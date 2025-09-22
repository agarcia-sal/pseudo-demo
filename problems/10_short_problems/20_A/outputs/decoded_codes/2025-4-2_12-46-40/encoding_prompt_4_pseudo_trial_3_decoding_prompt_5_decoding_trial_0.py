import re

def normalize_path(input_path):
    # Normalize the input path (resolution of relative paths is context-dependent and may require os.path)
    # Here, we'll just return the input for simplicity.
    return input_path.replace('//', '/')  # Simple normalization example

def remove_leading_slashes(path, retain_count):
    # Replace multiple leading slashes with a single leading slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    else:
        return path.lstrip('/')

# Read input from standard input
raw_input = input()

# Normalize the file path to remove any redundant separators
normalized_path = normalize_path(raw_input)

# Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
final_path = remove_leading_slashes(normalized_path, 1)

# Output the final formatted file path
print(final_path)

# Test cases (to be run separately)
# input: "//usr//local///bin" should output: "/usr/local/bin"
# input: "///etc//hosts" should output: "/etc/hosts"
# input: "var/www" should output: "var/www"
