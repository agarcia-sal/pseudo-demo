def normalize_path(path):
    # Normalize the path by changing backslashes to forward slashes
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    # Remove leading slashes by replacing multiple leading '/' with a single '/'
    while path.startswith('/'):
        path = path[1:]
    return path

# Read input from the standard input (stdin)
input_path = input()

# Normalize the file path
normalized_path = normalize_path(input_path)

# Remove leading slashes from the normalized file path
final_path = remove_leading_slashes(normalized_path)

# Output the final modified file path
print(final_path)
