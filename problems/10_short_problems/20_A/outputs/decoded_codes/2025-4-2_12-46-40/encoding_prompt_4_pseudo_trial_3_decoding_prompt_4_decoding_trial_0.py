import os
import re

def normalize_path(input_path):
    """
    Normalize the input file path by resolving relative paths and removing unnecessary separators.
    """
    # Use os.path.normpath to normalize the path according to the operating system's conventions
    normalized_path = os.path.normpath(input_path)
    return normalized_path

def remove_leading_slashes(path, retain_count):
    """
    Remove leading slashes from the path, ensuring that only one leading slash is retained.
    """
    # Use regex to replace multiple leading slashes with a single slash
    return re.sub(r'^/{2,}', '/', path)

# Read input from standard input
raw_input = input()

# Normalize the file path
normalized_path = normalize_path(raw_input)

# Ensure the path starts with a single '/' if it has any leading slashes
final_path = remove_leading_slashes(normalized_path, retain_count=1)

# Output the final formatted file path
print(final_path)
