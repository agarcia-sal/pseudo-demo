import os
import re

def normalize_path(input_string):
    # Remove leading and trailing whitespace from the input string
    trimmed_input_string = input_string.strip()

    # Normalize the path to a standard format
    normalized_path = os.path.normpath(trimmed_input_string)

    # Replace any sequence of leading slashes with a single slash
    updated_path = re.sub(r'^/+', '/', normalized_path)

    return updated_path

def main():
    # Read input from standard input
    input_string = input()

    # Normalize and process the path
    final_path = normalize_path(input_string)

    # Output the final transformed path
    print(final_path)

if __name__ == "__main__":
    main()
