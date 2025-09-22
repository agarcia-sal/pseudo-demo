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

def normalize_path(input_path):
    # Normalize the input path to remove any redundant separators
    return posixpath.normpath(input_path)

def replace_multiple_leading_slashes_with_single_slash(input_path):
    # Remove multiple leading slashes, keeping only one
    return regular_expression_replace(input_path)

def regular_expression_replace(input_path):
    # Use a regular expression to replace leading slashes
    return re.sub('^/+', '/', input_path)

# Example of how to use the function (uncomment to use):
# normalize_and_clean_path()
