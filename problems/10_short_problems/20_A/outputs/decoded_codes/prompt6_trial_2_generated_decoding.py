def normalize_file_path(file_path):
    # Remove leading forward slashes from the file path
    while file_path.startswith('/'):
        file_path = file_path[1:]

    # Normalize the file path by replacing any sequences of forward slashes with a single forward slash
    normalized_path = file_path.replace('//', '/')
    while '//' in normalized_path:
        normalized_path = normalized_path.replace('//', '/')

    return normalized_path

# Read input from user and store it as a string
user_input = input()

# Normalize the file path by calling the function
normalized_path = normalize_file_path(user_input)

# Print the resulting normalized path
print(normalized_path)
