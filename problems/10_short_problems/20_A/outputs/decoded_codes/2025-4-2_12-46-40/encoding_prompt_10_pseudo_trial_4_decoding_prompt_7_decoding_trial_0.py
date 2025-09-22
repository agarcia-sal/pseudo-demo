import re
import os

def main():
    # Step 1: Read input from system standard input
    input_string = read_from_standard_input()

    # Step 2: Normalize the path
    normalized_path = normalize_path(input_string)

    # Step 3: Remove leading slashes from the normalized path
    cleaned_path = remove_leading_slashes(normalized_path)

    # Step 4: Print the cleaned path
    print(cleaned_path)

def read_from_standard_input():
    # Reads the entire input from the standard input and returns it as a string
    return input()

def normalize_path(path):
    # Normalizes the path to a standard POSIX format
    # This handles things like resolving '..' and '.' in the path
    return os.path.normpath(path)

def remove_leading_slashes(path):
    # Replaces one or more leading slashes with a single slash
    return re.sub(r'^/+','/', path)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
