import os
import re

def normalize_and_print_path():
    # Read input from standard input
    raw_input = input()
    
    # Normalize the input path
    normalized_path = normalize_path(raw_input)
    
    # Print the modified path, replacing multiple leading slashes with a single slash
    print(replace_leading_slashes(normalized_path))

def normalize_path(raw_input: str) -> str:
    # Remove any leading or trailing whitespace from the input
    trimmed_input = raw_input.strip()
    
    # Normalize the file path using os.path.normpath to handle '.', '..', etc.
    normalized_path = os.path.normpath(trimmed_input)
    
    return normalized_path

def replace_leading_slashes(path: str) -> str:
    # Use a regular expression to replace multiple leading slashes with a single slash
    modified_path = re.sub(r'^/+', '/', path)
    
    return modified_path

# A simple test case execution
if __name__ == "__main__":
    normalize_and_print_path()
