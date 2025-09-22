from typing import Optional
import logging
import subprocess
import numpy as np
import os
from omegaconf import DictConfig

from utils.utils import *
from utils.llm_client.base import BaseClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ReEvo:
    def __init__(
            self,
            cfg: DictConfig,
            root_dir: str,
            stage: str, 
            round: int,
            timestamp: str, 
            generator_llm: BaseClient,
            reflector_llm: Optional[BaseClient] = None,
    ) -> None:
        self.cfg = cfg
        self.generator_llm = generator_llm
        self.reflector_llm = generator_llm
        self.root_dir = root_dir
        self.stage = stage
        self.round = round
        self.timestamp = timestamp
 
        self.mutation_rate = cfg.mutation_rate
        self.iteration = 0
        self.function_evals = 0 #not sure if i need this for my purposesx
        self.elitist = None
        self.long_term_reflection_str = ""
        self.best_obj_overall = None
        self.best_prompt_overall = None
        self.best_prompt_path_overall = None
        self.seed_func = ''
        self.problems_dir_name = ''

        self.init_prompt()
        self.init_population()


    def init_prompt(self) -> None:
        self.problem = self.cfg.problem.problem_name
        self.problem_size = self.cfg.problem.problem_size # not sure yet where this is needed
        self.difficulty = self.cfg.problem.problem_difficulty
        # self.func_name = self.cfg.problem.func_name   I dont think this is needed?

        logging.info("Problem: " + self.problem)

        self.prompt_dir = f"{self.root_dir}/prompts"
        self.problems_dir_name = '10_short_problems' # [TO DO] : figure out how to pass this in as an argument? the same way that the type of problem is passed in
        self.output_file = f"{self.root_dir}/problems/{self.problems_dir_name}/gpt_{self.stage}.txt" # might need to make the directory


        # Common prompts
        self.system_generator_prompt = file_to_string(f'{self.prompt_dir}/common/system_generator_{self.stage}.txt')
        self.system_reflector_prompt = file_to_string(f'{self.prompt_dir}/common/system_reflector_{self.stage}.txt')
        self.user_reflector_st_prompt = file_to_string(f'{self.prompt_dir}/common/user_reflector_st_{self.stage}.txt')  # shrot-term reflection
        self.user_reflector_lt_prompt = file_to_string(f'{self.prompt_dir}/common/user_reflector_lt_{self.stage}.txt') # long-term reflection
        self.crossover_prompt = file_to_string(f'{self.prompt_dir}/common/crossover.txt')
        self.mutation_prompt = file_to_string(f'{self.prompt_dir}/common/mutation.txt')
        self.user_generator_prompt = file_to_string(f'{self.prompt_dir}/common/user_generator_{self.stage}.txt')
        self.seed_prompt = file_to_string(f'{self.prompt_dir}/common/seed_{self.stage}.txt')
        if self.round == 0:
            self.seed_func = file_to_string(f'{self.prompt_dir}/common/initial_{self.stage}_prompt.txt')
            
        else:
            self.seed_func = file_to_string(f'{self.root_dir}/outputs/prompts/{self.timestamp}/{self.stage}_round_{self.round-1}.txt')

        self.seed_prompt = file_to_string(f'{self.prompt_dir}/common/seed_{self.stage}.txt').format(
            seed_func=self.seed_func,
        )

        # Flag to print prompts
        self.print_crossover_prompt = True # Print crossover prompt for the first iteration
        self.print_mutate_prompt = True # Print mutate prompt for the first iteration
        self.print_short_term_reflection_prompt = True # Print short-term reflection prompt for the first iteration
        self.print_long_term_reflection_prompt = True # Print long-term reflection prompt for the first iteration

    def init_population(self) -> None:
        # Evaluate the seed function, and set it as Elite
        logging.info("Evaluating seed function...")
        # user = self.seed_func + '\n' + get_pseudocode() # need to fix the directory of where pseudocode is generated and stored
        logging.info("Seed prompt: \n"+self.seed_func)
        prompt = ""
        
        seed_ind = {
            "stdout_filepath": f"{self.stage}_iter_{self.iteration}_round_{self.round}_stdout_0.txt", # [TO DO]: figure out how iterations are working
            "prompt": self.seed_func, 
            "prompt_path": f"{self.stage}_iter_{self.iteration}_round_{self.round}_prompt_0.txt", # [TO DO]: figure out how to update the prompt paths and if this is the correct path
            "response_id": 0,
        }
       
        self.seed_ind = seed_ind
        self.population = self.evaluate_population([seed_ind])

        # If seed function is invalid, stop
        if not self.seed_ind["exec_success"]:
            raise RuntimeError(f"Seed function is invalid. Please check the stdout file in {os.getcwd()}.")

        # Set seed function as elite:
        self.update_iter()

        # Generate responses
        system = self.system_generator_prompt
        user = self.user_generator_prompt + "\n" + self.seed_prompt + "\n" + self.long_term_reflection_str
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        logging.info("Initial Population Prompt: \nSystem Prompt: \n" + system + "\nUser Prompt: \n" + user)

        responses = self.generator_llm.multi_chat_completion([messages], self.cfg.init_pop_size, temperature = self.generator_llm.temperature + 0.3) # Increase the temperature for diverse initial population
        population = [self.response_to_individual(response, response_id) for response_id, response in enumerate(responses)]

        # Run code and evaluate population
        population = self.evaluate_population(population)

        # Update iteration
        self.population = population
        self.update_iter()

    def response_to_individual(self, response: str, response_id: int, file_name: str=None) -> dict:
        """
        Convert LLM response to individual
        """
        # Write response to file
        file_name = f"{self.stage}_{self.iteration}_round_{self.round}_response_{response_id}.txt" if file_name is None else file_name + ".txt"
        with open(file_name, 'w') as file:
            file.writelines(response + '\n')

        # code = extract_code_from_generator(response)
        prompt = response

        # Extract code and description from response
        std_out_filepath = f"{self.stage}_iter_{self.iteration}_round_{self.round}_stdout{response_id}.txt" if file_name is None else file_name + "_stdout.txt"
        
        individual = {
            "stdout_filepath": std_out_filepath,
            "prompt": prompt,
            "prompt_path": f"{self.stage}_iter_{self.iteration}_round_{self.round}_prompt_{response_id}.txt",
            "response_id": response_id,
        }

        return individual
    
    def mark_invalid_individual(self, individual: dict, traceback_msg: str) -> dict:
        """
        Mark an individual as invalid.
        """
        individual["exec_success"] = False
        individual["obj"] = float("inf")*-1.0
        individual["traceback_msg"] = traceback_msg
        return individual
    
    def evaluate_population(self, population: list[dict]) -> list[float]:
        """
        Evaluate population by running code in parallel and computing objective values.
        """
        inner_runs = []
        # Run code to evaluate
        for response_id in range(len(population)):
            self.function_evals += 1
            # Skip if response is invalid
            if population[response_id]["prompt"] is None:
                population[response_id] = self.mark_invalid_individual(population[response_id], "Invalid response!")
                inner_runs.append(None)
                continue
            
            logging.info(f"Iteration {self.iteration}: Running Code {response_id}")
            
            try:
                # print("population[response_id:]", population[response_id])
                process = self._run_prompt(population[response_id], response_id)
                inner_runs.append(process)
            except Exception as e: # If code execution fails
                logging.info(f"Error for response_id {response_id}: {e}")
                population[response_id] = self.mark_invalid_individual(population[response_id], str(e))
                inner_runs.append(None)
        
        # Update population with objective values
        for response_id, inner_run in enumerate(inner_runs):
            if inner_run is None: # If code execution fails, skip
                continue
            try:
                # print("right after the second try in evaluate_population()")
                # inner_run.communicate(timeout=self.cfg.timeout) # Wait for code execution to finish
                inner_run.communicate(timeout=600) # my timer needs to be way higher because the run_prompt is quite long
            except subprocess.TimeoutExpired as e:
                # print("am right after the second except in evaluate_population()")
                logging.info(f"Error for response_id {response_id}: {e}")
                population[response_id] = self.mark_invalid_individual(population[response_id], str(e))
                inner_run.kill()
                continue

            individual = population[response_id]
            stdout_filepath = individual["stdout_filepath"]
            with open(stdout_filepath, 'r') as f:  # read the stdout file
                stdout_str = f.read() 
            traceback_msg = filter_traceback(stdout_str)
            # print("traceback_msg: ", traceback_msg, "------!!!! end of traceback msg")
            
            individual = population[response_id]
            # Store objective value for each individual
            if traceback_msg == '': # If execution has no error
                try:
                    # print('in the 3rd? try, the one after the check for traceback_msg')
                    # print("stdout.split(\n):", stdout_str.split('\n'))
                    individual["obj"] = float(stdout_str.split('\n')[-2])
                    # print("right after trying to get the objective value")
                    individual["exec_success"] = True
                except:
                    # print("am in the except clause of the traceback_msg check")
                    population[response_id] = self.mark_invalid_individual(population[response_id], "Invalid std out / objective value!")
            else: # Otherwise, also provide execution traceback error feedback
                population[response_id] = self.mark_invalid_individual(population[response_id], traceback_msg)

            logging.info(f"Iteration {self.iteration}, response_id {response_id}: Objective value: {individual['obj']}")
        return population
    
    
    def _run_prompt(self, individual: dict, response_id) -> subprocess.Popen:
        """
        Feed prompt as encoding or the decoding and run eval script to get its objective value.
        """
        logging.debug(f"Iteration {self.iteration}: Processing Prompt Run {response_id}")
        # print(f"individual in _run_code(): ", individual)

        # output_file = individual["output_file"]
        
        with open(self.output_file, 'w') as file: # this output_file is gpt_[encoder/decoder.txt]
            file.writelines(individual["prompt"] + '\n') #this is where the error is!! code is: code: [```python`]

        # print("am about to run eval_prompt.py")
        # Execute the python file with flags
        with open(individual["stdout_filepath"], 'w') as f:
            eval_file_path = f'{self.root_dir}/problems/eval_prompt.py'
            process = subprocess.Popen(['python', '-u', eval_file_path, self.output_file, self.stage, self.root_dir, f'{self.round}', self.timestamp, 'train'],
                                        stdout=f, stderr=f)
            
        block_until_running(individual["stdout_filepath"], log_status=True, iter_num=self.iteration, response_id=response_id)
        return process
    
    def update_iter(self) -> None:
        """
        Update after each iteration
        """
        population = self.population
        objs = [individual["obj"] for individual in population]
        best_obj, best_sample_idx = max(objs), np.argmax(np.array(objs))
        
        # update best overall
        if self.best_obj_overall is None or best_obj > self.best_obj_overall:
            self.best_obj_overall = best_obj
            self.best_prompt_overall = population[best_sample_idx]["prompt"]
            self.best_prompt_path_overall = population[best_sample_idx]["prompt_path"]
        
        # update elitist
        if self.elitist is None or best_obj > self.elitist["obj"]: # [TO DO]: should I change best_obj > self.elitist.. to best_obj >= self.elitist ?
            self.elitist = population[best_sample_idx]
            logging.info(f"Iteration {self.iteration}: Elitist: {self.elitist['obj']}")
        
        logging.info(f"Iteration {self.iteration} finished...")
        logging.info(f"Best obj: {self.best_obj_overall}, Best Prompt Path: {self.best_prompt_path_overall}")
        logging.info(f"Function Evals: {self.function_evals}")
        self.iteration += 1

    def rank_select(self, population: list[dict]) -> list[dict]:
        """
        Rank-based selection, select individuals with probability proportional to their rank.
        """
        population = [individual for individual in population if individual["exec_success"]]

        if len(population) < 2:
            return None
        # Sort population by objective value
        maximize_obj = True if self.stage == 'decoder' else False
        # Below we will combine dominance-dissimilarity and line-count like so:
        # lambda * dominance-dissimilarity + (1-lambda) * line-count also phrased like this:
        # alpha * dominance-dissimilarity + beta * line_count with alpha + beta = 1
        # to start off with alpha = 0.9 and beta = 0.1 because the line count differences are quite big in magnitude
        alpha = 0.9
        beta = 0.1
        # obj_score = alpha * 

        # if self.stage == 'encoder':
            
        #     dominance_dissimilarity_vector = self.get_dominance_dissimilarity_matrix(population)
        #     population = sorted(population, key=lambda x: alpha* (dominance_dissimilarity_vector[x["response_id"] - 1]) + beta * x["obj"], reverse=False)
        # else:
        population = sorted(population, key=lambda x: x["obj"], reverse = True)

        ranks = [i for i in range(len(population))]
        probs = [1 / (rank + 1 + len(population)) for rank in ranks]
        # Normalize probabilities
        probs = [prob / sum(probs) for prob in probs]
        selected_population = []
        trial = 0
        while len(selected_population) < 2 * self.cfg.pop_size:
            trial += 1
            parents = np.random.choice(population, size=2, replace=False, p=probs)
            if parents[0]["obj"] != parents[1]["obj"]:
                selected_population.extend(parents)
            if trial > 1000:
                return None
        return selected_population
    
    def random_select(self, population: list[dict]) -> list[dict]:
        """
        Random selection, select individuals with equal probability.
        """
        selected_population = []
        # Eliminate invalid individuals
        population = [individual for individual in population if individual["exec_success"]]
        if len(population) < 2:
            return None
        trial = 0
        while len(selected_population) < 2 * self.cfg.pop_size:
            trial += 1
            parents = np.random.choice(population, size=2, replace=False)
            # If two parents have the same objective value, consider them as identical; otherwise, add them to the selected population
            if parents[0]["obj"] != parents[1]["obj"]:
                selected_population.extend(parents)
            if trial > 1000:
                return None
        return selected_population

    
    def gen_short_term_reflection_prompt(self, ind1: dict, ind2: dict) -> tuple[list[dict], str, str]:
        """
        Short-term reflection before crossovering two individuals.
        """
        if ind1["obj"] == ind2["obj"]:
            # print(ind1["prompt"], ind2["prompt"])
            raise ValueError("Two individuals to crossover have the same objective value!")
        # Determine which individual is better or worse
        if ind1["obj"] > ind2["obj"]:
            better_ind, worse_ind = ind1, ind2
        elif ind1["obj"] < ind2["obj"]:
            better_ind, worse_ind = ind2, ind1

        worse_prompt = worse_ind["prompt"]
        better_prompt = better_ind["prompt"]
        
        system = self.system_reflector_prompt
        user = self.user_reflector_st_prompt.format(
            worse_prompt=worse_prompt,
            better_prompt=better_prompt
            )
        message = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        
        # Print reflection prompt for the first iteration
        if self.print_short_term_reflection_prompt:
                logging.info("Short-term Reflection Prompt: \nSystem Prompt: \n" + system + "\nUser Prompt: \n" + user)
                self.print_short_term_reflection_prompt = False
        return message, worse_prompt, better_prompt
    
    def short_term_reflection(self, population: list[dict]) -> tuple[list[list[dict]], list[str], list[str]]:
        """
        Short-term reflection before crossovering two individuals.
        """
        messages_lst = []
        worse_prompt_lst = []
        better_prompt_lst = []
        for i in range(0, len(population), 2):
            # Select two individuals
            parent_1 = population[i]
            parent_2 = population[i+1]
            
            # Short-term reflection
            messages, worse_prompt, better_prompt = self.gen_short_term_reflection_prompt(parent_1, parent_2)
            messages_lst.append(messages)
            worse_prompt_lst.append(worse_prompt)
            better_prompt_lst.append(better_prompt)
        
        # Asynchronously generate responses
        response_lst = self.reflector_llm.multi_chat_completion(messages_lst)
        return response_lst, worse_prompt_lst, better_prompt_lst
    
    def long_term_reflection(self, short_term_reflections: list[str]) -> None:
        """
        Long-term reflection before mutation.
        """
        system = self.system_reflector_prompt
        user = self.user_reflector_lt_prompt.format(
            prior_reflection = self.long_term_reflection_str,
            new_reflection = "\n".join(short_term_reflections),
            )
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        
        if self.print_long_term_reflection_prompt:
            logging.info("Long-term Reflection Prompt: \nSystem Prompt: \n" + system + "\nUser Prompt: \n" + user)
            self.print_long_term_reflection_prompt = False
        
        self.long_term_reflection_str = self.reflector_llm.multi_chat_completion([messages])[0]
        
        # Write reflections to file
        file_name = f"problem_iter_{self.iteration}_short_term_reflections.txt"
        with open(file_name, 'w') as file:
            file.writelines("\n".join(short_term_reflections) + '\n')
        
        file_name = f"problem_iter_{self.iteration}_long_term_reflection.txt"
        with open(file_name, 'w') as file:
            file.writelines(self.long_term_reflection_str + '\n')
    
    def crossover(self, short_term_reflection_tuple: tuple[list[list[dict]], list[str], list[str]]) -> list[dict]:
        reflection_content_lst, worse_code_lst, better_code_lst = short_term_reflection_tuple
        messages_lst = []
        for reflection, worse_prompt, better_prompt in zip(reflection_content_lst, worse_code_lst, better_code_lst):
            # Crossover
            system = self.system_generator_prompt
            user = self.crossover_prompt.format(
                user_generator = self.user_generator_prompt,
                worse_prompt = worse_prompt,
                better_prompt = better_prompt,
                reflection = reflection,
            )
            messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
            messages_lst.append(messages)
            
            # Print crossover prompt for the first iteration
            if self.print_crossover_prompt:
                logging.info("Crossover Prompt: \nSystem Prompt: \n" + system + "\nUser Prompt: \n" + user)
                self.print_crossover_prompt = False
        
        # Asynchronously generate responses
        response_lst = self.generator_llm.multi_chat_completion(messages_lst)
        crossed_population = [self.response_to_individual(response, response_id) for response_id, response in enumerate(response_lst)]

        assert len(crossed_population) == self.cfg.pop_size
        return crossed_population
    
    def mutate(self) -> list[dict]:
        """Elitist-based mutation. We only mutate the best individual to generate n_pop new individuals."""
        system = self.system_generator_prompt
        user = self.mutation_prompt.format(
            user_generator = self.user_generator_prompt,
            reflection = self.long_term_reflection_str,
            elitist_prompt = self.elitist["prompt"],
        )
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        if self.print_mutate_prompt:
            logging.info("Mutation Prompt: \nSystem Prompt: \n" + system + "\nUser Prompt: \n" + user)
            self.print_mutate_prompt = False
        responses = self.generator_llm.multi_chat_completion([messages], int(self.cfg.pop_size * self.mutation_rate))
        population = [self.response_to_individual(response, response_id) for response_id, response in enumerate(responses)]
        return population

    def evolve(self):
        # while self.function_evals < self.cfg.max_fe:
        while self.function_evals < 80:
            # If all individuals are invalid, stop
            if all([not individual["exec_success"] for individual in self.population]):
                raise RuntimeError(f"All individuals are invalid. Please check the stdout files in {os.getcwd()}.")
            # Select
            population_to_select = self.population if (self.elitist is None or self.elitist in self.population) else [self.elitist] + self.population # add elitist to population for selection
            print("population_to_select:", population_to_select)
            selected_population = self.rank_select(population_to_select)
            if selected_population is None:
                raise RuntimeError("Selection failed. Please check the population.")
            # Short-term reflection
            short_term_reflection_tuple = self.short_term_reflection(selected_population) # (response_lst, worse_code_lst, better_code_lst)
            # Crossover
            crossed_population = self.crossover(short_term_reflection_tuple)
            print("crossed_population: ", crossed_population)
            # Evaluate
            self.population = self.evaluate_population(crossed_population)
            print("evaluated crossed population: ", self.population)
            # Update
            self.update_iter()
            # Long-term reflection
            self.long_term_reflection([response for response in short_term_reflection_tuple[0]])
            # Mutate
            mutated_population = self.mutate()
            print("mutated population: ", mutated_population)
            # Evaluate
            self.population.extend(self.evaluate_population(mutated_population))
            # Update
            self.update_iter()
        return self.best_prompt_overall, self.best_prompt_path_overall
    
    
    
    



