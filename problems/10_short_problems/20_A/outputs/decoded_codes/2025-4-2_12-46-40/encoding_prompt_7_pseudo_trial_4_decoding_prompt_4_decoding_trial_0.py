import posixpath
import re

def normalize_and_clean_path():
    # Read a path from standard input
    read_path = input()

    # Normalize the path by removing any redundant separators
    normalized_path = normalize_path(read_path)

    # Clean up the path to ensure it starts with a single forward slash
    cleaned_path = replace_multiple_leading_slashes_with_single_slash(normalized_path)

    # Print the cleaned path
    print(cleaned_path)

def normalize_path(input_path: str) -> str:
    # Normalize the input path to remove any redundant separators
    return posixpath.normpath(input_path)

def replace_multiple_leading_slashes_with_single_slash(input_path: str) -> str:
    # Remove multiple leading slashes, keeping only one
    return regular_expression_replace(input_path)

def regular_expression_replace(input_path: str) -> str:
    # Use a regular expression to replace leading slashes
    return re.sub(r'^/+','/', input_path)

# Entry point for the program
if __name__ == "__main__":
    normalize_and_clean_path()
