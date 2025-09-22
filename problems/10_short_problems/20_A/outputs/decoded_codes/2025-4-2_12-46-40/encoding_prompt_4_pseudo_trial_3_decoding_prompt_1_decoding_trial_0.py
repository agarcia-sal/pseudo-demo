def normalize_path(input):
    # This function would typically resolve relative paths and
    # remove unnecessary separators. 
    # For demonstration, we'll just replace backslashes with slashes
    # and ignore other normalization logic for simplicity.
    return input.replace('\\', '/').strip()

def remove_leading_slashes(path, retain_count):
    # Replace multiple leading slashes with a single slash
    while len(path) > retain_count and path.startswith('/'):
        path = path[1:]
    return '/' + path if path else path

# Read input from standard input
raw_input = input()

# Normalize the file path to remove any redundant separators
normalized_path = normalize_path(raw_input)

# Use a regular expression (or string manipulation) to ensure the path
# starts with a single '/' if it contains any leading slashes
final_path = remove_leading_slashes(normalized_path, 1)

# Output the final formatted file path
print(final_path)
