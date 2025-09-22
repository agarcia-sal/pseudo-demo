import re

def normalize_path(input_path):
    # Normalize the path by resolving relative paths and removing unnecessary separators
    normalized_path = re.sub(r'/+', '/', input_path)  # Replace multiple slashes with a single one
    return normalized_path

def remove_leading_slashes(path, retain_count):
    # Replace multiple leading slashes with a single slash, maintaining the amount specified by retain_count
    new_path = re.sub(r'^/{%d,}' % (retain_count + 1), '/', path)  # Replace leading slashes
    return new_path

# Read input from standard input
raw_input = input()

# Normalize the file path to remove any redundant separators
normalized_path = normalize_path(raw_input)

# Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
final_path = remove_leading_slashes(normalized_path, 1)

# Output the final formatted file path
print(final_path)
