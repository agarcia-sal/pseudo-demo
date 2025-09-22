import os
import sys
import re

def normalize_file_path(input_string):
    # Normalize the file path using the os.path.normpath method
    normalized_path = os.path.normpath(input_string)

    # Replace multiple leading slashes with a single slash using regular expressions
    result_path = re.sub(r'^/{2,}', '/', normalized_path)

    return result_path

def main():
    # Read input from standard input
    input_string = input()
    
    # Process the input string to normalize the path and replace leading slashes
    result_path = normalize_file_path(input_string)
    
    # Output the final result
    print(result_path)

if __name__ == "__main__":
    main()
