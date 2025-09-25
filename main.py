import hydra
import logging 
import os
from pathlib import Path
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import cProfile
import pstats
import traceback
from utils.utils import init_client, file_to_string, setup_dataset, minify_code
from evaluation.utils import save_metrics, save_prompt, get_pseudocode_dataset, evaluate_classifier_prompt, save_classifier_score, record_previous_best_solution, get_avg_test_case_length, get_num_difficulty, copy_difficulty_problems, get_positive_labels, write_dataset_to_file, write_error_strings_to_file, reformat_human_eval_file
# from agents import GreedyRefine
from evaluation import Evaluator, get_data
from openai import OpenAI


ROOT_DIR = os.getcwd()
logging.basicConfig(level=logging.INFO)

def run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round):
    # Write file to outputs/prompts directory so that next stage can load in the file
    best_prompt_path = f"{ROOT_DIR}/outputs/prompts/{timestamp}/{stage}_round_{round}.txt"
    with open(best_prompt_path, 'w') as file: 
        file.writelines(best_prompt_overall + '\n')
    # Run validation and redirect stdout to a file "best_code_overall_stdout.txt"
    with open(f"{ROOT_DIR}/problems/{problems_dir_name}/gpt_{stage}.txt", 'w') as file: #[TO DO]: not sure what this is for
        file.writelines(best_prompt_overall + '\n')
    test_script = f"{ROOT_DIR}/problems/eval_prompt.py" # instead, the eval script will compare the outputs
    # to the correct intputs and print out how many of the tests were passed
    test_script_stdout = "best_code_overall_val_stdout.txt"
    logging.info(f"Running validation script...: {test_script}")
    with open(test_script_stdout, 'w') as stdout:
        subprocess.run(["python", test_script, best_prompt_path, stage, ROOT_DIR, f'{round}', timestamp, 'val'], stdout=stdout)
    logging.info(f"Validation script finished. Results are saved in {test_script_stdout}.")

    # Print the results
    with open(test_script_stdout, 'r') as file:
        for line in file.readlines():
            logging.info(line.strip())

@hydra.main(version_base=None, config_path="cfg", config_name="config")
def main(cfg):
    workspace_dir = Path.cwd()
    # Set logging level
    logging.info(f"Workspace: {workspace_dir}")
    logging.info(f"Project Root: {ROOT_DIR}")
    # logging.info(f"Using LLM: {cfg.get('model', cfg.llm_client.model)}")
    logging.info(f"Using LLM: {cfg.llm_client.model}")
    logging.info(f"Using Algorithm: {cfg.algorithm}")

    client = init_client(cfg)

    print('client: ', client)

    if cfg.algorithm == "reevo":
        from reevo import ReEvo as ga
    elif cfg.algorithm == "greedy":
        from agents.greedy_refine import GreedyRefine as ga # [TO DO]: change ga as agent; figure out how to blend the two
#         agent = GreedyRefine(
#         timeout=10,
#         model='openai/o3-mini', # We use LiteLLM to call API
# )
    else:
        raise NotImplementedError
    
    # Main algorithm
    problems_dir_name = 'human_eval'
    # problems_dir_name = 'leet_code'
    # problems_dir_name = 'cosmetic_pseudocodes'
    # problems_dir_name = 'classifier_pseudocodes'
    if problems_dir_name == 'leet_code':
        # version = 'v0.1.0'
        version = 'v0.3.0-hard'
        # version = 'v3rd100'
        # version = 'v0.3.0tiny'
        split = 'train'
        # problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        problems_filename = f'LeetCodeDataset-{version}-{split}.jsonl'
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    elif problems_dir_name == "cosmetic_pseudocodes":
        # previous_timestamp = '2025-09-18_21-00-18'
        # previous_timestamp = '2025-09-18_04-55-13'
        previous_timestamp = '2025-09-24_15-05-02'
        problems_filename = f"positive_labels_{previous_timestamp}.jsonl"
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    elif problems_dir_name == "classifier_pseudocodes":
        version = 2
        problems_filename = f"LeetCode-pseudo-v0.{version}.0-train.jsonl"
        # train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    else:
        split = "train"
        problems_filename = f'HumanEval-{split}.jsonl'
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')


    print('problems_filename:')
    print(problems_filename)

    starting_iteration = 1
    iterations = 32# [TO DO]: CO-Bench paper uses 64
    rounds = 2# [TO DO]: this is a hyperparameter i need to tune; am using 10 for now
    timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp
    

    load_previous = False
    if load_previous:
        timestamp = '2025-09-13_12-15-28'
    
    evolving_encoding = False # depends on whether we are continuing in the encoding or decoding
    evolving_decoding = False # This should start off as False always
    evolving_cosmetic = False
    evolving_classifier = False

    if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
        setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 2) # plus 2 because of the final encoder and decoder verification at the end

    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}") # [TO DO]: decide if i still need this
    generated_prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"


        # previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{iteration}", "previous_best", previous_best.json)
    # print(f"Directory '{generated_prompts_path}' created successfully")
    # print('prompt path: ', str(generated_prompts_path))

    # client = OpenAI(
    #     # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    #     api_key = os.getenv('OPENAI_API_KEY'),
    # )
   

    encoding_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='encoder'
    )
    decoding_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='decoder'
    )

    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")
    prev_encoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")

    if load_previous and (evolving_encoding or evolving_decoding):
        # if starting_iteration % 8 <= 4: # encoding stage
        #     encoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{starting_iteration - 1}", "previous_best", "previous_best.json")
        # else:
        prev_encoder_iter = 9 # [TO DO]: CHANGE
        encoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_encoder_iter}", "previous_best", "previous_best.json")
        encoding_agent.load_previous(encoding_previous_best_path) # [TO DO]: write load_previous() function
        # prev_decoder_iter = 0
        # prev_decoder_filename = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_decoder_iter}", "prompts", "decoder_stage_decoding_prompt.txt")
        # prev_decoder_prompt = file_to_string(prev_decoder_filename)
        if starting_iteration >= (rounds + 2):
            # if starting_iteration % 8 > 4:
            prev_decoder_iter = 8 # [TO DO]: CHANGE
            decoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_decoder_iter}", "previous_best", "previous_best.json")
            decoding_agent.load_previous(decoding_previous_best_path)
            prev_encoder_prompt = encoding_agent.finalize()
            # prev_encoder_iter = 0
            # prev_encoder_filename = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_encoder_iter}", "prompts", "encoder_stage_encoding_prompt.txt")
            # prev_encoder_prompt = file_to_string(prev_encoder_filename)
        if starting_iteration >= (2*rounds + 1): # After at least one round of decoding 
            prev_decoder_prompt = decoding_agent.finalize()
        
    if load_previous and evolving_cosmetic:
        prev_cosmetic_iter = 0 

    evaluator = Evaluator(data, timeout=5) # [TO DO]: change timeout
        

    # profiler = cProfile.Profile()
    # profiler.enable()

    # Run for 20/64 iterations
    for it in range(starting_iteration, iterations + 1):
        # Encoding:
        # print(f'iteration: {it}')
        if evolving_encoding:
            stage = 'encoder'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # for round in range(rounds):
                print('right before calling agent.step()')
                prompt = encoding_agent.step()
                print('right after calling agent.step()')
                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    # print('prompt is none')
                    break
                print('right before calling evaluate()')
                feedback = evaluator.evaluate(prompt, prev_decoder_prompt, stage, timestamp, it, client)  # Run evaluation
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                
                
                # print('feedback: ', feedback)
                print('right before calling feedback() within the round')
                encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback = encoding_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback)
                print('right after calling feedback() within the round')
                # Get the final solution
                # print('right before calling finalize()')
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = encoding_agent.finalize()
                    prev_encoder_prompt = best_prompt_so_far
                # print('right after calling fnalize()')
                # if feedback.dev_score == 1.0:
                #     print('prompt: ')
                #     print(prompt)
                #     break
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                traceback.print_exc()
                continue  # Skip to the next round
        if evolving_decoding:
            stage = 'decoder'
            try:
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # for round in range(rounds):
                # print('in decoding round:', round)
                prompt = decoding_agent.step()
                if prompt is None:  # agent decides to terminate
                    break # [TO DO]: or should this be 'continue'??
                feedback = evaluator.evaluate(prompt, prev_encoder_prompt, stage, timestamp, it, client)  # Run evaluation
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                
                # [TO DO]: add a try except or catch error when there is not an encoder prompt returned
                decoding_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                # Record Previous best
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback = decoding_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback)
                # Get the final solution
                # print('right before calline finalize()')
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = decoding_agent.finalize()
                    prev_decoder_prompt = best_prompt_so_far

            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round
        if (evolving_encoding or evolving_decoding) and it % rounds == 0: # maybe start at iterations = 1 ? and put this at the bottom of the loop
            evolving_encoding = not evolving_encoding
            evolving_decoding = not evolving_decoding

    # Finalize:
    if (evolving_encoding or evolving_decoding):
        print('finalize section:')
        print('encoding:')
        prompt = encoding_agent.finalize()
        save_prompt(str(generated_prompts_path), prompt, iterations + 1, 'encoder')
        feedback = evaluator.evaluate(prompt, prev_decoder_prompt, 'encoder', timestamp, iterations + 1, client)
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, 'encoder', iterations + 1)
        # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics: [TO DO]!

        print('decoding:')
        prompt = decoding_agent.finalize()
        save_prompt(str(generated_prompts_path), prompt, iterations + 2, 'decoder')
        feedback = evaluator.evaluate(prompt, prev_encoder_prompt, 'decoder', timestamp, iterations + 2, client)
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, 'decoder', iterations + 2)
    # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics [TO DO]!

    # profiler.disable()

    # Save results to file
    # stats = pstats.Stats(profiler)
    # stats.dump_stats('profile_results.prof')
    # stats.print_stats()
    # stats.sort_stats('time').print_stats(20)

    # print('best encoding prompt: ')
    # print(prev_encoder_prompt)
    # print('best decoder prompt:')
    # print(prev_decoder_prompt)

    ######################## Store pseudocode in a pandas dataframe: ################################
    problems_dir = f"{ROOT_DIR}/data/{problems_dir_name}"
    # avg_test_case_num = get_avg_test_case_length(os.path.join(problems_dir, problems_filename))
    # print("avg num of test cases: ", avg_test_case_num)
    start = 1
    end = 3000
    difficulty = "Hard"
    # for v0.3.0 in first 800, there is 165 Hard, 444 Medium, and 190 Easy
    # in next 800, 801 through 1600, there is 177 Hard, 416 Medium, and 208 Easy
    # ok in total there are ony 532 Hard...
    # for v0.3.0 test, there are 108 Hard and 188 Medium. ok let's try to do a 50/50 split
    # new_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
    # num_difficulty_problems = get_num_difficulty(os.path.join(problems_dir, new_filename), difficulty, start, end)
    # print(f"number of problems with difficulty {difficulty} is: ", num_difficulty_problems)
    # Get hard pseudocodes
    difficulty_map = {"Hard": 400, "Medium": 400}
    limit = 800
    new_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
    # copy_difficulty_problems(os.path.join(problems_dir, problems_filename), os.path.join(problems_dir, new_filename), difficulty_map, limit)

    store_pseudocode = False
    if store_pseudocode:
        print('in store pseudocode')
        stage = 'encoder'
        # timestamp = '2025-06-16_14-15-27'
        first_timestamp = '' # <- passing rate + natural language + conciseness
        # first_timestamp = '2025-09-18_21-00-18' # <- passing rate + natural language
        # first_timestamp = '2025-09-18_04-55-13'
        # first_timestamp = '2025-09-18_21-00-18'
        first_timestamp = '2025-09-24_15-05-02'
        first_dir_name = 'human_eval'
        first_pipeline_json_path_name = f"{ROOT_DIR}/data/{first_dir_name}/metrics/{first_timestamp}_metrics.json"
        # second_timestamp =  '2025-09-18_21-00-18' # <- just readability: avg_word_length - avg_words_per_line
        # second_timestamp =  '2025-09-19_11-38-47'
        # second_timestamp =  '2025-09-20_00-16-56'
        second_timestamp =  '2025-09-24_18-22-37'
        # second_timestamp =  '2025-09-20_19-13-22'
        second_dir_name = 'cosmetic_pseudocodes'
        # second_dir_name = 'leet_code'
        second_pipeline_json_path_name = f"{ROOT_DIR}/data/{second_dir_name}/metrics/{second_timestamp}_metrics.json"
        # problems_dir_file_name = "HumanEval.jsonl"
        # problems_filename = f'LeetCodeDataset-v0.3.0tiny-train.jsonl'
        # problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        # problems_dir = f"{ROOT_DIR}/data/{first_dir_name}"
        # first_problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        first_problems_filename = f'HumanEval-train.jsonl'
        first_dir = f"{ROOT_DIR}/data/{first_dir_name}"
        second_dir = f"{ROOT_DIR}/data/{second_dir_name}"
        second_problems_filename = f"positive_labels_{first_timestamp}.jsonl"
        # second_problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        # positive_labels_path_name = os.path.join(ROOT_DIR, "outputs", "pseudocodes", f"positive_labels_{timestamp}")
        # GET POSITIVE EXAMPLES:
        # first_timestamp = '2025-09-18_21-00-18'
        first_timestamp = '2025-09-24_15-05-02'
        
        new_file_name = os.path.join(ROOT_DIR, "data", "cosmetic_pseudocodes", f"positive_labels_{first_timestamp}.jsonl")
        # positive_examples = get_positive_labels(first_pipeline_json_path_name, first_dir, first_problems_filename, new_file_name, first_timestamp)
        # positive_examples = get_positive_labels(first_pipeline_json_path_name, problems_dir, problems_filename, first_timestamp, iterations)
        
        # GET PSEUDOCODE DATASET FOR THE CLASSIFIER:
        limit = 150
        problem_results, dev_set_results = get_pseudocode_dataset(first_pipeline_json_path_name, second_pipeline_json_path_name, first_dir, second_dir, first_problems_filename, second_problems_filename, first_timestamp, second_timestamp, iterations, limit)
        # print('problem_results: ')
        # print(problem_results)
        # print('dev_set_results:')
        # print(dev_set_results)
        # true_positive_examples, true_negative_examples, near_miss_examples, near_pass_examples = results
        version = 2
        # train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        # write_dataset_to_file(problem_results, train_set_filename)
        # write_dataset_to_file(dev_set_results, dev_set_filename)
        # write_dataset_to_file(positive_examples, positive_examples_file_name)
        # [TO DO]: add near-misses, and near-passes as something i get from the pseudocode dataset
        # For train:
        previous_timestamp = '2025-09-18_04-55-13'
        final_iter = 34
        decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")
        version = 2
        file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        # file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        version = 3
        new_file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        # new_file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        # write_error_strings_to_file(file_name, new_file_name, decoder_prompt, client)
        # split = "test"
        # problems_filename = f'HumanEval-{split}.jsonl'
        # file_name = os.path.join(ROOT_DIR, "data", "human_eval", problems_filename)
        # reformat_human_eval_file(file_name)

    ######################## Create cosmetic changes for the positive labels: ################################

    cosmetic_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='cosmetic'
    )
    # evolving_cosmetic = True
    cosmetic_iterations = 32

    if load_previous and evolving_cosmetic:
        prev_iter = 0
        cosmetic_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_iter}", "previous_best", "previous_best.json")
        cosmetic_agent.load_previous(cosmetic_previous_best_path)

    evaluator_cosmetic = Evaluator(data, timeout=5) # [TO DO]: change timeout
    # positive_examples_file_name = os.path.join(ROOT_DIR, "outputs", "pseudocodes", f"positive_labels_{timestamp}.jsonl")
    final_iter = 34
    # previous_timestamp = '2025-09-18_21-00-18'
    # previous_timestamp = '2025-09-18_04-55-13'
    previous_timestamp = '2025-09-24_15-05-02'
    positive_examples_file_name = f"positive_labels_{previous_timestamp}.jsonl"
    decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")

    #[TO DO]: set up dataset and metrics path and everything else.

    for it in range(1, cosmetic_iterations+1):
        # Encoding:
        if evolving_cosmetic:
            stage = 'cosmetic'
            try: # may hit an LLM rate limite
                
                # print('right before calling agent.step()')
                prompt = cosmetic_agent.step()
                # print('step:', 0)
                # print('right after calling agent.step()')
                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    print('prompt is none')
                    break
                print('right before calling evaluate() within the round')
                feedback = evaluator_cosmetic.evaluate_cosmetic(prompt, decoder_prompt, stage, timestamp, it, client)
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                
                # [TO DO]: add a try except or catch error when there is not an encoder prompt returned
                cosmetic_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                # Record Previous best:
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback = cosmetic_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback)

                #######################################################################
              
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round

    ######################## Run the classifier: ####################################################
    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
    generated_prompts_path.mkdir(parents=True, exist_ok=True)

    version = 3
    train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
    dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
    classifier_dataset_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes")
    classifier_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='classifier'
    )
    # evolving_classifier = False
    classifier_iterations = 7
    # rounds = 1
    previous_timestamp = '2025-09-18_21-00-18'
    final_iter = 34
    decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")

    evaluator_classifier = Evaluator(data, timeout=5)

    for it in range(1, classifier_iterations + 1):
        # Encoding:
        if evolving_classifier:
            stage = 'classifier'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # print('right before calling agent.step()')
                prompt = classifier_agent.step()
                # print('step:', 0)
                # print('right after calling agent.step()')
                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    # print('prompt is none')
                    break
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                # print('right before calling evaluate() within the round')
                # feedback = evaluator_classifier.evaluate_classifier(prompt, decoder_prompt, stage, timestamp, it, client)
                mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client, decoder_prompt, classifier_dataset_name, timestamp, it)
                # mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client, decoder_prompt, classifier_dataset_name, timestamp, it)
                # print('step:', 1)
                feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
                # feedback = evaluator_classifier.get_feedback_classifier(mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
                # print('step:', 2)
                score = feedback.dev_score
                # save_metrics(avg_metrics, metrics_path, timestamp, stage, it, round, rounds)
                # save_classifier_score(score, metrics_path, timestamp, stage, it)
                # print('step:', 3)
                
                # print('step:', 4)
                # print('feedback: ', feedback)
                # print('right before calling feedback() within the round')
                classifier_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback = classifier_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback)

                # print('step:', 5)
                # print('right after calling feedback() within the round')
                # Get the final solution
                # print('right before calling finalize()')
                # print('right after calling save_metrics()')
                # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics: [TO DO]!
                # if feedback.dev_score == 1.0:
                #     print('prompt: ')
                #     print(prompt)
                #     break
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round

    # [TO DO]: do a final accuracy check on the final prompt. oh but isnt that evaluate_classifier_prompt() should do above?
    # test the final prompt with the TEST dataset
    
    # if evolving_classifier:
    #     # test final classifier prompt with dev_set and test_set
    #     prompt = classifier_agent.finalize()
    #     save_prompt(str(generated_prompts_path), prompt, classifier_iterations+1, stage)
    #     save_prompt(str(generated_prompts_path), prompt, classifier_iterations+2, stage)
    #     # train score:
    #     mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client)
    #     feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, final_score, metrics)  # Run evaluation
    #     avg_metrics = feedback.avg_metrics
    #     save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+1)
    #     # dev score:
    #     dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl" )
    #     mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, final_score, metrics = evaluate_classifier_prompt(dev_set_filename, prompt, client)
    #     dev_feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, final_score, metrics)  # Run evaluation
    #     avg_metrics = dev_feedback.avg_metrics
    #     save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+2)

        # test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-test.jsonl" )
        # test_score = evaluate_classifier_prompt(test_set_filename, prompt, client)
        # test_feedback = evaluator.get_feedback_classifier(test_score)
        # avg_metrics = feedback.avg_metrics
        # save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
        #[TO DO]: add adding metrics to evaluator.get_feedback
        #[TO DO]: check on save_classifier_score
        #[TO DO]: check that finalize has all the correct things, it has dev_score but should also have validation score
    
        # print('avg_metrics: ', avg_metrics)
        # save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+1)
        # save_classifier_score(dev_score, metrics_path, timestamp, "classifier", classifier_iterations+1)
    # print('pseudocode_dataset_list: ')
    # print(pseudocode_dataset_list)

    # profiler.disable()
    # profiler.print_stats(sort='time') 
    # profiler.dump_stats('profile_data.prof') 
    # stats = pstats.Stats('profile_data.prof')
    # stats.strip_dirs().sort_stats('time').print_stats(10)  # show top 10 by internal time          
    # Plot:
    # Load results
    # problems_dir_path = Path(f"{ROOT_DIR}/data/{problems_dir_name}")
    # problems = [problem.name for problem in problems_dir_path.iterdir() if (problem.is_dir() and problem.name != 'metrics')]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "max_passing_rate"]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "passing_rate", "avg_score"]
    # metrics = ["line_count", "passing_rate", "avg_score"]
    # print('problems: ', problems)
    # problems = ["2_C", "9_E", "39_E", "42_B", "53_E", "69_D", "121_C", "132_C", "193_E", "200_C"] #long
    # problems = ["2_C", "9_E", "39_E", "42_B", "53_E"]
    # problems = ["8_B", "8_E", "9_D", "14_E", "16_B", "17_A", "18_A", "27_E", "30_B", "31_E"] # medium
    # problems = ["17_A", "18_A", "27_E", "30_B", "31_E"]
    # problems = ["11_B", "20_A", "23_A", "26_A", "32_B", "32_C", "39_D", "41_C", "43_B", "55_A"]
    problems = ["11_B", "20_A", "23_A", "26_A", "32_B"]
    problems = ["HumanEval/0", "HumanEval/1", "HumanEval/2", "HumanEval/3", "HumanEval/4"]
    problems = ["two-sum", "add-two-numbers", "longest-substring-without-repeating-characters", "median-of-two-sorted-arrays", "zigzag-conversion"]
    # problems = ["32_C", "39_D", "41_C", "43_B", "55_A"]
    metrics = ["avg_score", "passing_rate"]
    # metrics = ['line_length']
    # metrics.extend(problems)
    # print('metrics: ', metrics)
    # metrics = ["line_count"]
    # timestamp = '2025-06-19_14-18-09'
    # timestamp = '2025-06-16_14-15-27'
    # timestamp = '2025-06-19_17-37-11'

    timestamp = '2025-09-15_01-29-56' # readability: "avg_syllables_per_word", "line_count"]
    timestamp = '2025-09-18_21-00-18'
    timestamp = '2025-09-24_15-05-02'
    # problems_dir_name = 'leet_code'
    problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    with open(problem_metrics_file, "r") as f:
        data = json.load(f)
    df_enc_2 = pd.DataFrame(data)

    # metrics = ["passing_rate", "avg_word_length", "avg_words_per_line"]
    # metrics = ["passing_rate", "avg_syllables_per_word", "avg_words_per_line"]
    metrics = ["passing_rate"]
    # metrics = ["passing_rate", "avg_word_length"]
    # metrics = ["avg_score"]

    plt.figure(2)  # Use a different figure number
    ax2 = df_enc_2.plot(
        x="iter",              # X-axis
        y=metrics,                         # Y-columns (as a list)
        figsize=(10, 5),                   # Figure size
        title="Metrics Over Time - Autoencoder - HumanEval",  # Plot title
        grid=True,                         # Show grid
        marker="o"                         # Marker style
    )

    plt.tight_layout()
    plt.show()
    ###########################################

    # categories = ['Datasets', 'Agent Frameworks']
    # categories = ['GreedyRefine', 'DirectAnswer']

    # This is the dataset figure
    # Data for the visualization
    # datasets = ['GreedyRefine', 'DirectAnswer']
    # metrics = ['avg_score', 'avg_passing_rate', 'avg_word_length', 
    #         'classifier_accuracy_rate_validation', 'classifier_accuracy_rate_test']

    # leetcode_data = {
    #     'avg_score': 0.75,
    #     'avg_passing_rate': 0.68,
    #     'avg_word_length': 42.5,
    #     'classifier_accuracy_rate_validation': 0.82,
    #     'classifier_accuracy_rate_test': 0.79
    # }

    # humaneval_data = {
    #     'avg_score': 0.63,
    #     'avg_passing_rate': 0.57,
    #     'avg_word_length': 38.2,
    #     'classifier_accuracy_rate_validation': 0.76,
    #     'classifier_accuracy_rate_test': 0.72
    # }

    
    # leetcode_values = [leetcode_data[metric] for metric in metrics] # Convert to arrays for easier plotting
    # humaneval_values = [humaneval_data[metric] for metric in metrics]

    # fig, ax2 = plt.subplots(figsize=(16, 8))
    # fig.suptitle('Performance Comparison: LeetCode vs HumanEval', fontsize=16, fontweight='bold')

    # Second subplot: Grouped bar chart for detailed comparison
    # x = np.arange(len(metrics))
    # width = 0.35

    # bars1 = ax2.bar(x - width/2, leetcode_values, width, label='LeetCode', color='#1f77b4', alpha=0.8)
    # bars2 = ax2.bar(x + width/2, humaneval_values, width, label='HumanEval', color='#ff7f0e', alpha=0.8)

    # ax2.set_xlabel('Metrics')
    # ax2.set_ylabel('Values')
    # # ax2.set_title('Detailed Metric Comparison')
    # ax2.set_xticks(x)
    # ax2.set_xticklabels(metrics, rotation=45, ha='right')
    # ax2.legend()

    # # Add value labels on bars
    # def add_value_labels(bars, ax):
    #     for bar in bars:
    #         height = bar.get_height()
    #         ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
    #                 f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    # add_value_labels(bars1, ax2)
    # add_value_labels(bars2, ax2)

    # plt.tight_layout()
    # plt.show()

    # Additional visualization: Side-by-side metrics table
    # fig, ax = plt.subplots(figsize=(12, 4))
    # ax.axis('tight')
    # ax.axis('off')

    # table_data = []
    # for metric in metrics:
    #     table_data.append([metric, f"{leetcode_data[metric]:.3f}", f"{humaneval_data[metric]:.3f}"])

    # table = ax.table(cellText=table_data,
    #                 colLabels=['Metric', 'LeetCode', 'HumanEval'],
    #                 cellLoc='center',
    #                 loc='center',
    #                 colColours=['#f0f0f0', '#d0e5ff', '#ffe5cc'])

    # table.auto_set_font_size(False)
    # table.set_fontsize(10)
    # table.scale(1, 1.5)

    # plt.title('Metric Values Comparison', fontsize=14)
    # plt.show()

    # filtered_df_2 = df_enc_2[df_enc_2['stage'] == 'encoder']
    # max_index = filtered_df_2['avg_score'].idxmax()
    # max_row = filtered_df_2.loc[max_index]

    # print("for avg_word_length, avg_words_per_line :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # plt.show()


    # classifier_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_classifier_metrics.json"
    # with open(classifier_metrics_file, "r") as f:
    #     classifier_data = json.load(f)

    # decoding_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_decoder_metrics.json"
    # with open(decoding_metrics_file, "r") as f:
    #     decoding_data = json.load(f)

    #### Encoding Metrics
    # timestamp = '2025-09-11_22-54-06' # readability: "avg_word_length", "avg_words_per_line"
    # timestamp = '2025-09-11_11-17-39' # readability: "avg_word_length", "line_count"
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # # plt.figure(1)
    # # df.plot(x="round", y="max_passing_rate")

    # metrics = ["passing_rate", "avg_word_length", "line_count"]

    # # Create the second plot with metrics
    # plt.figure(1)  # Use a different figure number
    # ax1 = df_enc.plot(
    #     x="iter",              # X-axis
    #     y=metrics,                         # Y-columns (as a list)
    #     figsize=(10, 5),                   # Figure size
    #     title="Metrics Over Time - Encoding",  # Plot title
    #     grid=True,                         # Show grid
    #     marker="o"                         # Marker style
    # )

    # filtered_df = df_enc[df_enc['stage'] == 'encoder']
    # max_index = filtered_df['avg_score'].idxmax()
    # max_row = filtered_df.loc[max_index]

    # print("for avg_word_length :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # timestamp = '2025-09-12_11-31-03' # readability: "avg_syllables_per_word", "avg_words_per_line"]
    # timestamp = '2025-09-10_19-53-08' # readability: "avg_syllables_per_word", "line_count"]
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc_2 = pd.DataFrame(data)

    # metrics = ["passing_rate", "avg_syllables_per_word", "line_count"]

    # plt.figure(2)  # Use a different figure number
    # ax2 = df_enc_2.plot(
    #     x="iter",              # X-axis
    #     y=metrics,                         # Y-columns (as a list)
    #     figsize=(10, 5),                   # Figure size
    #     title="Metrics Over Time - Encoding",  # Plot title
    #     grid=True,                         # Show grid
    #     marker="o"                         # Marker style
    # )

    # filtered_df_2 = df_enc_2[df_enc_2['stage'] == 'encoder']
    # max_index = filtered_df_2['avg_score'].idxmax()
    # max_row = filtered_df_2.loc[max_index]

    # print("for avg_syllables_per_word :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # plt.show()

    # df_enc = pd.DataFrame(encoding_data)
    # df.plot(x="round", y="max_passing_rate")
    # plt.figure(1)
    # ax1 = df_enc.plot(
    #     x="iteration-rounds",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Metrics Over Time - Encoding",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # # Customize the plot
    # ax1.set_xlabel("Iteration-Rounds")
    # ax1.set_ylabel("Value")
    # plt.legend(title="Metrics")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_metrics.png")
    # timestamp = '2025-09-06_13-14-33'
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # def create_metric_figure(metrics_subset, fig_title):
    #     """Helper function to create a figure for a subset of metrics"""
    
    # for ax, metric in zip(axes, metrics_subset):

    # fig1, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    # axes = axes.flatten()


    # for ax, problem in zip(axes, problems):
    #     for i in range(len(df_enc)-1): # First, plot the BASELINE_METRIC - avg score (in all subplots)
    #         color = 'gray'  # Distinct color for baseline
    #         alpha = 0.5  # Make it semi-transparent
    #         ax.plot(
    #             df_enc['iter'].iloc[i:i+2],
    #             df_enc['avg_score'].iloc[i:i+2],
    #             color=color,
    #             linestyle=':',
    #             alpha=alpha,
    #             marker='d'  # Diamond marker for baseline
    #         )
        # Second, plot the BASELINE_METRIC - passing rate (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'purple'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['passing_rate'].iloc[i:i+2],
        #         color=color,
        #         linestyle='--',
        #         alpha=alpha,
        #         marker='x'  # Diamond marker for baseline
        #     )

        # Next, plot each problem metric in its own subplot
        # for i in range(len(df_enc)-1):
        #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
        #     marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc[problem+"_avg_syllables_per_word"].iloc[i:i+2],
        #         color + '-',
        #         marker=marker
        #     )
        
        # ax.set_title(problem)
        # ax.grid(True)

    # Add common legend
    # handles = [
    #     plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Avg Syllables per word'),
    #     # plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
    #     plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
    #     plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    # ]
    # fig1.legend(handles=handles, loc='lower center', ncol=2)

    # Fig 2:

    # fig2, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    # axes = axes.flatten()


    # for ax, problem in zip(axes, problems):
        # First, plot the BASELINE_METRIC - avg score (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'gray'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['avg_score'].iloc[i:i+2],
        #         color=color,
        #         linestyle=':',
        #         alpha=alpha,
        #         marker='d'  # Diamond marker for baseline
        #     )
        # Second, plot the BASELINE_METRIC - passing rate (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'purple'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['passing_rate'].iloc[i:i+2],
        #         color=color,
        #         linestyle='--',
        #         alpha=alpha,
        #         marker='x'  # Diamond marker for baseline
        #     )

        # Next, plot each problem metric in its own subplot
        # for i in range(len(df_enc)-1):
        #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
        #     marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc[problem+f"_passing_rate"].iloc[i:i+2],
        #         color + '-',
        #         marker=marker
        #     )
        
        # ax.set_title(problem)
        # ax.grid(True)

    # Add common legend
    # handles = [
    #     # plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Avg Score'),
    #     plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
    #     plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
    #     plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    # ]
    # fig2.legend(handles=handles, loc='lower center', ncol=2)

    # fig1.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_avg_syllables_per_word.png", bbox_inches='tight', dpi=300)
    # fig2.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_passing_rate.png", bbox_inches='tight', dpi=300)

    # plt.tight_layout()
    # plt.show()
    ##########
    # problem = '41_C'
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # colors = ['b' if df_enc['stage'].iloc[i] == 'encoder' else 'r' for i in range(len(df_enc))]
    # markers = ['o' if df_enc['stage'].iloc[i] == 'encoder' else 's' for i in range(len(df_enc))]
    # passing_rates = [df_enc[problem].iloc[i] for i in range(len(df_enc))]
    # iters = [df_enc['iter'].iloc[i] for i in range(len(df_enc))]
    # print('passing_rates:', passing_rates)
    # print('iters:', iters)

    # for i in range(len(df_enc)-1):
    #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
    #     plt.plot(
    #         df_enc['iter'].iloc[i:i+2],
    #         df_enc[problem].iloc[i:i+2], # passing rate for this specific problem
    #         color + '-',
    #         marker='o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
    #     )
    # for x, y, color, marker in zip(iters, passing_rates, colors, markers):
    #     plt.scatter(x, y, c=color, marker=marker, s=100)

    # # Connect points with a line (optional)
    # plt.plot(iters, passing_rates, 'k-', alpha=0.3)  # gray connecting line

    # # Create custom legend
    # import matplotlib.lines as mlines
    # blue_line = mlines.Line2D([], [], color='blue', marker='o', linestyle='-', label='Encoder')
    # red_line = mlines.Line2D([], [], color='red', marker='s', linestyle='-', label='Decoder')
    # plt.legend(handles=[blue_line, red_line])

    # # Add labels and title
    # plt.xlabel('Number of Iterations')
    # plt.ylabel('Passing Rate')
    # plt.title('Passing Rate by Stage Across Iterations')
    # plt.grid(True)

    # # Show the plot
    # plt.show()

    ### Decoding Metrics
    # df_dec = pd.DataFrame(decoding_data)
    # # df.plot(x="round", y="max_passing_rate")
    # plt.figure(2)
    # ax2 = df_dec.plot(
    #     x="iteration-rounds",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Metrics Over Time - Decoding",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # Customize the plot
    # ax2.set_xlabel("Iteration-Rounds")
    # ax2.set_ylabel("Value")
    # plt.legend(title="Metrics")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_decoder_metrics.png")
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_decoder_metrics.png")


    ### Classifier Metrics
    # df_clas = pd.DataFrame(classifier_data)
    # # df.plot(x="round", y="max_passing_rate")
    # plt.figure(1)
    # ax1 = df_clas.plot(
    #     x="iter",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Score Over Time - Classifier",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # # # Customize the plot
    # ax1.set_xlabel("Iterations")
    # ax1.set_ylabel("Value")
    # plt.legend(title="Score")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_metrics.png")
    # plt.show()



if __name__ == "__main__":
    main()