import re
import os
import sys

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
    return sys.stdin.read().strip()  # Read input from standard input and remove leading/trailing whitespace


def normalize_path(path):
    # Normalize the path to a POSIX-compliant format using os.path.normpath
    return os.path.normpath(path)


def remove_leading_slashes(path):
    # Replace one or more leading slashes with a single slash using regular expressions
    return re.sub(r'^/+', '/', path)


if __name__ == "__main__":
    main()
