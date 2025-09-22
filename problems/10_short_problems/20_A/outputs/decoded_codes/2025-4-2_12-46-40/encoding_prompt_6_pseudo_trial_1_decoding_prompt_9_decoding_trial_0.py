def normalize_file_path(raw_file_path):
    # Trim whitespace from the input
    trimmed_file_path = remove_whitespace(raw_file_path)

    # Normalize the file path by removing unnecessary segments
    normalized_file_path = remove_redundant_path_segments(trimmed_file_path)

    # Ensure the normalized path starts with a single forward slash
    final_file_path = ensure_single_leading_slash(normalized_file_path)

    return final_file_path

def remove_whitespace(file_path):
    # Remove leading and trailing whitespace from the filePath
    return file_path.strip()

def remove_redundant_path_segments(file_path):
    # Replace multiple sequential slashes (//) with a single slash (/)
    while '//' in file_path:
        file_path = file_path.replace('//', '/')
    return file_path

def ensure_single_leading_slash(file_path):
    if file_path.startswith('/'):
        return file_path  # Already has a leading slash
    else:
        return '/' + file_path  # Add a leading slash

# Read the input from standard input
user_input = input()

# Normalize the file path
result_path = normalize_file_path(user_input)

# Print the final normalized file path
print(result_path)
