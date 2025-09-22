import re
import os

def read_from_standard_input():
    # Read a string from the standard input
    return input()

def normalize_path(path):
    # Normalize the file system path to a standard POSIX format
    return os.path.normpath(path)

def remove_leading_slashes(path):
    # Use regular expressions to replace leading slashes with a single slash
    return re.sub(r'^/+','/', path)

def main():
    # Step 1: Read input from the standard input
    input_string = read_from_standard_input()
    
    # Step 2: Normalize the path
    normalized_path = normalize_path(input_string)
    
    # Step 3: Remove leading slashes from the normalized path
    cleaned_path = remove_leading_slashes(normalized_path)
    
    # Step 4: Print the cleaned path
    print(cleaned_path)

if __name__ == "__main__":
    main()
