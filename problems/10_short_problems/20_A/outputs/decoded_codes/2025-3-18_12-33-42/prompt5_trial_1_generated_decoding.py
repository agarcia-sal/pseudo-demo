def normalize_file_path(input_string):
    # Remove leading and trailing white spaces from the input
    trimmed_input = input_string.strip()
    
    # Normalize the path by removing unnecessary components
    normalized_path = remove_redundant_path_elements(trimmed_input)
    
    # Ensure the path starts with a single leading slash
    final_path = ensure_single_leading_slash(normalized_path)
    
    return final_path

def remove_redundant_path_elements(path):
    # Replace multiple consecutive slashes with a single slash
    path_with_single_slashes = '/'.join(part for part in path.split('/') if part)
    
    return path_with_single_slashes

def ensure_single_leading_slash(path):
    # If the path starts with multiple slashes, replace them with a single leading slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    else:
        return '/' + path

# Read input from standard input
input_from_user = input()

# Normalize the file path
output_path = normalize_file_path(input_from_user)

# Print the output path
print(output_path)
