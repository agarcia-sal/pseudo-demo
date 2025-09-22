import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
from utils.utils import file_to_string

ROOT_DIR = os.getcwd()


def main():
    # 1. Load input and expected output
    input_file_path = f"{ROOT_DIR}/problems/10_short_problems/11_B/test_cases/1_input.txt"
    expected_output_file_path = f"{ROOT_DIR}/problems/10_short_problems/11_B/test_cases/1_output.txt"
    with open(input_file_path, 'r') as f:
        input_data = f.read()
    with open(expected_output_file_path, 'r') as f:
        expected_output = f.read()

    # 2. Prepare the environment
    local_namespace = {
        'input_data': input_data,  # Pass input as a variable
        '__name__': '__main__'     # Optional: Handle if __name__ checks exist
    }

    code = file_to_string(f"{ROOT_DIR}/problems/10_short_problems/11_B/llm_scripting/starter_code.py")
    
    print('loaded in code, here it is:')
    print(code)

    # 3. Capture stdout/stderr
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    print('right after the stdout and stderror capture lines')

    # 4. Execute the code with redirected I/O
    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            print('write before running exec()')
            exec(code, local_namespace)
            print('right after runninge exec()')
    except Exception as e:
        return False, f"Execution failed: {str(e)}"

    # 5. Compare outputs
    actual_output = stdout_capture.getvalue()
    if actual_output.strip() == expected_output.strip():
        return True, "Output matches!"
    else:
        return False, f"Output mismatch.\nExpected:\n{expected_output}\nGot:\n{actual_output}"
    

if __name__ == "__main__":
    result = main()
    print(result)