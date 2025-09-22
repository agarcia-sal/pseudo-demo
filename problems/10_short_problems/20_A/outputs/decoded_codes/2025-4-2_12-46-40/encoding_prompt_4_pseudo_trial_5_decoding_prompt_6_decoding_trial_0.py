def normalize_path(path):
    # Normalize the path by replacing backslashes with forward slashes
    return path.replace('\\', '/')


def remove_leading_slashes(path):
    # Remove leading slashes and replace them with a single slash
    return '/' + path.lstrip('/')


# Read input from the standard input (stdin)
input_path = input()

# Normalize the file path
normalized_path = normalize_path(input_path)

# Remove leading slashes from the normalized file path
final_path = remove_leading_slashes(normalized_path)

# Output the final modified file path
print(final_path)
