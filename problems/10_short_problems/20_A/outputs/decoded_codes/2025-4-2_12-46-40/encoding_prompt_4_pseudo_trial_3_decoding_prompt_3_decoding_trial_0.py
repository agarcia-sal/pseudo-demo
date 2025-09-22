import os
import re

def normalize_path(input_path):
    # Normalize the input path by resolving relative paths and removing unnecessary separators.
    return os.path.normpath(input_path)

def remove_leading_slashes(path, retain_count):
    # Replace multiple leading slashes with a single slash.
    return re.sub(r'^(/{2,})', '/', path, count=1)  # Only keeps one leading slash

# Read input from standard input
raw_input = input()

# Normalize the file path to remove any redundant separators
normalized_path = normalize_path(raw_input)

# Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
final_path = remove_leading_slashes(normalized_path, 1)

# Output the final formatted file path
print(final_path)
