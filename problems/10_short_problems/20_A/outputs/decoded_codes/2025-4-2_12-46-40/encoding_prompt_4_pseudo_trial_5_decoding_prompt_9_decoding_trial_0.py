import os

# Function to normalize the file path
def normalize_path(path):
    # Replace backslashes with forward slashes
    return path.replace('\\', '/')

# Function to remove leading slashes from the path
def remove_leading_slashes(path):
    # Checking if there are leading slashes and replacing them with a single slash
    while path.startswith('/'):
        path = path[1:]
    return '/' + path if path else path  # Ensure at least one leading slash is retained if path remains

# Read input from the standard input (stdin)
input_path = input()

# Normalize the file path
normalized_path = normalize_path(input_path)

# Remove leading slashes from the normalized file path
final_path = remove_leading_slashes(normalized_path)

# Output the final modified file path
print(final_path)
