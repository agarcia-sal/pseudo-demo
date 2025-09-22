import os
# from evaluation.utils import FileLock, ParallelRun, design_optimal, eval_all, filter_dev, filter_test, normalize_metrics, average_metrics, check_if_no_metrics, get_problem_scores, get_num_test_cases, run_test_case
from datetime import datetime
from pathlib import Path
import subprocess

ROOT_DIR = os.getcwd()

def get_num_test_cases(problem_file_path):
    test_cases_folder = Path(problem_file_path) / "test_cases"
    num_test_cases = sum(1 for item in test_cases_folder.iterdir() if "input" in item.name)
    return num_test_cases

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        # Process each line, split into tokens, and strip unwanted chars
        processed = []
        for line in file:
            processed.extend(token.strip(' (,)') for token in line.split())
        return processed

def compare_outputs(file_path_expected, file_path_stdout):
    list_expected = read_file_to_list(file_path_expected)
    list_stdout = read_file_to_list(file_path_stdout)
    # print("list expected: ", list_expected)
    # print("list stdout: ", list_stdout)
    return list_expected == list_stdout
    
def run_test_case(problem_file_path, code_solution_path, idx, timestamp, iter, stage, error_file_path):
    input_file_path = os.path.join(problem_file_path, "test_cases", f"{idx}_input.txt")
    output_file_path = os.path.join(problem_file_path, "test_cases", f"{idx}_output.txt")
    stdout_file_path = os.path.join(problem_file_path, "outputs", "stdouts", f"{idx}_stdout.txt")
    # error_file_path = f"{problem_path}/outputs/errors/{timestamp}/decoding_prompt_{decoding_prompt_num}_trial_{trial}_test_case_{i}.txt"
    # error_file_path = os.path.join(problem_file_path, "outputs", "errors", timestamp, f"iter_{iter}_error_{idx}_{stage}.txt") # [TO DO]: change!!
    timeout = 5
    num_correct = 0
    num_errors = 0
    try:

        with open(input_file_path, 'r') as input_file, open(stdout_file_path, 'w') as output_file, open(error_file_path, 'w') as error_file:
            result = subprocess.run(["python3", code_solution_path], stdin=input_file, stdout=output_file, stderr=error_file, timeout=10) #capture stdout and stderr

        # if result.returncode == 0:
        #     print("Script ran successfully.")
        # else:
        #     print("Script failed:", result.stderr)
        if result.returncode != 0:
            print(f"Script failed with return code {result.returncode}. Check the error file at {error_file_path} for details.\n")
            num_errors += 1
            # if num_errors == 2:
            #     break # if there is an error for one trial, there must be an error for the other trials
        # else: # delete the file cause it's taking up too much space
            # If the script succeeded, delete the error file
            # if os.path.exists(error_file_path):
            #     os.remove(error_file_path)
                # print(f"Script succeeded. Deleted the error file at {error_file_path}.")

        # Compare the captured output with the contents of the output file
        with open(output_file_path, "r") as f:
            expected_output = f.read()
        if compare_outputs(output_file_path, stdout_file_path):
        # Comparing the result's stdout to the expected output
        # if result.stdout == expected_output:
            # print("Output matches the expected output.")
            num_correct = 1
    except subprocess.TimeoutExpired:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        with open(error_file_path, 'a') as file:
            file.write(f"Script timed out after {timeout} seconds.")
            file.write("------------------------------------------\n")
        print(f"Script timed out after {timeout} seconds.")
    except subprocess.CalledProcessError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Script failed with error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("Script failed with error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    except FileNotFoundError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("File not found error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    except Exception as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Unexpected error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("Unexpected error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    return num_correct, output_file_path, stdout_file_path

if __name__ == '__main__':

    problems_dir_name = '10_short_problems'
    problem_name = '41_C'
    iter = 1
    stage = 'decoder'
    iterations = 4 # [TO DO]: CO-Bench paper uses 64
    rounds = 1 # [TO DO]: this is a hyperparameter i need to tune; am using 10 for now
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"
    now = datetime.now()
    timestamp = f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}"
    # setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}")



    problem_file_path = os.path.join(ROOT_DIR, "data", problems_dir_name, problem_name)
    code_solution_path = os.path.join(ROOT_DIR, "testing", "code.py")
    results_path = os.path.join(ROOT_DIR, "testing", "code_results.txt")
    error_file_path = os.path.join(ROOT_DIR, "testing", "code_error.txt") # [TO DO]: change!!

    # what do i need?
    num_test_cases = get_num_test_cases(problem_file_path)
    num_correct = 0

    with open(results_path, 'w') as file:
        for idx in range(num_test_cases):
            # print('is this for loop even being run?')
            result, output_file_path, stdout_file_path = run_test_case(problem_file_path, code_solution_path, idx+1, timestamp, iter, stage, error_file_path) # [TO DO]: check if run_test_case() returns error or exception at some point
            file.write(f'Output for idx {idx+1}: {result}\n')
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

