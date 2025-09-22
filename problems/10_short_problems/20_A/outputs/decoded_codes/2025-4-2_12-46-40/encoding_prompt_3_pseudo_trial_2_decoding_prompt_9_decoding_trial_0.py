def normalize_path(path_string):
    # Normalize the path to ensure it has a proper format
    # This example just simulates normalization; actual logic may vary
    normalized_path = path_string.replace("\\", "/")  # Example normalization
    return normalized_path

def remove_leading_slashes(path_string):
    # Replace any leading slashes at the start of the string with a single slash
    while path_string.startswith('/'):
        path_string = path_string[1:]
    return '/' + path_string if path_string else path_string  # Ensure at least one slash

# Main logic flow
raw_path = input()  # Read input from standard input

# Normalize the path
normalized_path = normalize_path(raw_path)

# Remove leading slashes from the normalized path
final_path = remove_leading_slashes(normalized_path)

# Print the resulting path
print(final_path)
