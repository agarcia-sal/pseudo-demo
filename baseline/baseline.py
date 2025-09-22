import logging 
import subprocess
import os
import time

code = ''

ROOT_DIR = os.getcwd()
logging.basicConfig(level=logging.INFO)

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip newline characters, and store in a set
        temp_list = file.read().split()
        return [elt.strip() for elt in temp_list]
        # return list(line.strip() for line in file if line.strip())

def compare_outputs(file_path_1, file_path_2):
    list_1 = read_file_to_list(file_path_1)
    list_2 = read_file_to_list(file_path_2)
    # print("list 1: ", list_1)
    # print("list 2: ", list_2)

    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            return False
    return True

def main():
    # Set logging level
    logging.info(f"Project Root: {ROOT_DIR}")
    
    # Main algorithm
    # problems_list = ['2-fast-2-furious', 'a-problem-on-string', 'abed-and-timelines', 'add-subtract', 'battle-of-stalingrad']
    problems_list =  ['a-to-b-1']
    num_of_test_cases = 3

    for problem in problems_list:
        num_correct = 0
        problem_script = f"{ROOT_DIR}/baseline/problem/{problem}/gpt_complete.py"
        for i in range(1, num_of_test_cases + 1):
            input_file_path = f"{ROOT_DIR}/baseline/problem/{problem}/test_cases/{i}_input.txt"
            output_file_path = f"{ROOT_DIR}/baseline/problem/{problem}/test_cases/{i}_output.txt"
            stdout_file_path = f"{ROOT_DIR}/baseline/problem/{problem}/test_cases/{i}_stdout.txt"
            # result = ''

            start_time = time.time()
            with open(input_file_path, 'r') as input_file, open(stdout_file_path, 'w') as output_file:
                result = subprocess.run(["python3", problem_script], stdin=input_file, stdout=output_file, timeout=20) #capture stdout and stderr
            end_time = time.time()

            # print("Execution time:", end_time - start_time)
            # print("STDOUT:", result.stdout.decode())
            # print("STDERR:", result.stderr.decode())

            if result.returncode == 0:
                print("Script ran successfully.")
            else:
                print("Script failed:", result.stderr)

            # Compare the captured output with the contents of the output file
            with open(output_file_path, "r") as f:
                expected_output = f.read()
            if compare_outputs(output_file_path, stdout_file_path):
            # Comparing the result's stdout to the expected output
            # if result.stdout == expected_output:
                print("Output matches the expected output.")
                num_correct += 1
            else:
                print("Output does not match the expected output.")
        print(f"Problem {problem} passed {num_correct}/5 test cases.\n")


if __name__ == "__main__":
    main()