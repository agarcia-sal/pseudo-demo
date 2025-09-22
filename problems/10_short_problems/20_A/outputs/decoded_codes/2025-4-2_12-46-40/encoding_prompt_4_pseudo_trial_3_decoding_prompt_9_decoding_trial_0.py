import re

def normalize_path(input_path):
    # Normalize the input path (e.g., resolve relative paths, remove unnecessary separators)
    return re.sub(r'/+', '/', input_path.strip())

def remove_leading_slashes(path, retain_count):
    # Replace multiple leading slashes with a single slash, retaining the specified count
    if path.startswith('/'):
        # Keep one leading slash and any subsequent ones after that
        return '/' + path.lstrip('/')
    return path.lstrip('/')

# Read input from standard input
raw_input = input()

# Normalize the file path to remove any redundant separators
normalized_path = normalize_path(raw_input)

# Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
final_path = remove_leading_slashes(normalized_path, 1)

# Output the final formatted file path
print(final_path)
