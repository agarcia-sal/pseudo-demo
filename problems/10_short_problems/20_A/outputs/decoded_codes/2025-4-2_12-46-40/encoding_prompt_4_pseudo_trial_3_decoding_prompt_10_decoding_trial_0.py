import os
import re

def read_input():
    """Reads input from standard input."""
    return input()

def normalize_path(input_path):
    """
    Normalizes the input path by resolving relative paths 
    and removing unnecessary separators.
    """
    # Use os.path.normpath to normalize the path
    return os.path.normpath(input_path)

def remove_leading_slashes(path):
    """
    Replaces multiple leading slashes with a single slash.
    If the path contains any leading slashes, it retains only one.
    """
    # Use a regular expression to match leading slashes
    return re.sub(r'^/+', '/', path)

def main():
    # Step 1: Read the raw input from standard input
    raw_input = read_input()

    # Step 2: Normalize the file path
    normalized_path = normalize_path(raw_input)

    # Step 3: Remove leading slashes, keeping only one
    final_path = remove_leading_slashes(normalized_path)

    # Step 4: Output the final formatted file path
    print(final_path)

# Execute the main function when the script is called
if __name__ == "__main__":
    main()
