import os
import sys
import re
import textwrap
# from evaluation.utils import FileLock, ParallelRun, design_optimal, eval_all, filter_dev, filter_test, normalize_metrics, average_metrics, check_if_no_metrics, get_problem_scores, get_num_test_cases, run_test_case
from datetime import datetime
from test_code import run_test_case, get_num_test_cases
from openai import OpenAI
from dotenv import load_dotenv

ROOT_DIR = os.getcwd()

# module_dir = os.path.join(ROOT_DIR, "utils")

# # module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils"))
# sys.path.insert(0, module_dir)

# from utils.utils import file_to_string



# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("OPENAI_API_KEY")

def file_to_string(filename):
    with open(filename, 'r') as file:
        return file.read()

def extract_code_blocks(response):
    pattern_backticks = r"```python\s*(.*?)\s*```"
    pattern_dashes = r"^-{3,}\s*\n(.*?)\n-{3,}"
    blocks = re.findall(pattern_backticks, response, re.DOTALL)
    blocks.extend(re.findall(pattern_dashes, response, re.DOTALL | re.MULTILINE))
    return blocks

def call_llm(question: str, client, model='gpt-4.1-mini') -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model=model,
    )
    print('response:')
    print(response)

    answer = response.choices[0].message.content
    return answer

if __name__ == '__main__':

    client = OpenAI(
        # This is the default and can be omitted
        # api_key=os.environ.get("OPENAI_API_KEY"),
        api_key=api_key,
    )

    problems_dir_name = '10_short_problems'
    problem_name = '41_C'
    iter = 4
    stage = 'encoder'
    iterations = 1 # [TO DO]: CO-Bench paper uses 64
    rounds = 1 # [TO DO]: this is a hyperparameter i need to tune; am using 10 for now
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"
    now = datetime.now()
    timestamp = f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}"
    # minify_code(f"{ROOT_DIR}/data/{problems_dir_name}")
    # setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}")

    # encoder_prompt_path = os.path.join(ROOT_DIR, "testing", "encoder_prompt.txt")
    decoder_prompt_path = os.path.join(ROOT_DIR, "testing", "decoder_prompt.txt")
    problem_file_path = os.path.join(ROOT_DIR, "data", problems_dir_name, problem_name)
    code_solution_path = os.path.join(ROOT_DIR, "testing", "decoded_code.py")
    pseudocode_path = os.path.join(ROOT_DIR, "testing", "pseudocode.txt")
    results_path = os.path.join(ROOT_DIR, "testing", "pseudocode_results.txt")
    error_file_path = os.path.join(ROOT_DIR, "testing", "pseudocode_error.txt") # [TO DO]: change!!    

    # Step 1: Get decoded code
    decoder_prompt = file_to_string(decoder_prompt_path)
    pseudocode = file_to_string(pseudocode_path)
    question = decoder_prompt + "\nPseudocode to translate: " + pseudocode
    decoding = call_llm(question, client)
    print('decoding: ', decoding)
    code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
    if len(code_blocks) == 0:
        code_blocks = decoding # in case the prompt didn't output ```python``` formatting, is this the best way to do this?
    # print('code blocks in gen_multi_chat_decodings(): ', code_blocks)
    code = textwrap.dedent(code_blocks[0])
    print('code: ', code)

    with open(code_solution_path, 'w') as file:
        file.write(code)

    num_test_cases = get_num_test_cases(problem_file_path)
    num_correct = 0

    with open(results_path, 'w') as file:
        for idx in range(num_test_cases):
            # print('is this for loop even being run?')
            try: 
                # result = 1 #[TO DO]: change to below, and pass in timstamp, iter, round, stage
                result, output_file_path, stdout_file_path = run_test_case(problem_file_path, code_solution_path, idx+1, timestamp, iter, stage, error_file_path) # [TO DO]: check if run_test_case() returns error or exception at some point
                # print('result in try: ', result)
                num_correct += result
            except Exception as e:
                result = f"Exception: {str(e)}"
            file.write(f'Output for idx {idx+1}: {result}\n')
            # if os.path.exists(error_file_path):
            if os.path.exists(error_file_path) and os.path.getsize(error_file_path) != 0:
                file.write("Error:")
                with open(error_file_path, 'r') as error_file:
                    for line in error_file:
                        file.write(line)
                file.write('\n')
                os.remove(error_file_path)
            elif os.path.exists(error_file_path):
                os.remove(error_file_path)

            if result == 0: 
                with open(output_file_path, 'r') as output_file:
                    file.write("Expected:\n")
                    for line in output_file:
                        file.write(line)

                with open(stdout_file_path, 'r') as stdout_file:
                    file.write("Actual:\n")
                    for line in stdout_file:
                        file.write(line)
                file.write('\n')

        passing_rate = num_correct / num_test_cases
        file.write(f"passing rate: {passing_rate}")
