def normalize_path(path):
    # Normalize the path by removing redundant slashes
    # This could be a placeholder for built-in functionality or logic to actually normalize paths
    normalized_path = '/'.join(part for part in path.split('/') if part) # Removes empty parts
    return normalized_path

def replace_leading_slashes(path):
    # Ensure that the path starts with a single leading slash
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash

# Read input from standard input
input_string = input()

# Normalize the path by removing any redundant separators
normalized_path = normalize_path(input_string)

# Replace any leading slashes with a single slash
final_output = replace_leading_slashes(normalized_path)

# Print the final output
print(final_output)
