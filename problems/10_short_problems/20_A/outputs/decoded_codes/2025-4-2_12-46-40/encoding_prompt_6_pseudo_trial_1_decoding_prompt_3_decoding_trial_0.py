def normalize_file_path(raw_file_path):
    """
    Normalize the given file path by trimming whitespace, 
    removing redundant path segments, and ensuring it 
    starts with a single leading slash.
    """
    trimmed_file_path = remove_whitespace(raw_file_path)
    normalized_file_path = remove_redundant_path_segments(trimmed_file_path)
    final_file_path = ensure_single_leading_slash(normalized_file_path)
    
    return final_file_path

def remove_whitespace(file_path):
    """
    Remove leading and trailing whitespace from the file path.
    """
    return file_path.strip()

def remove_redundant_path_segments(file_path):
    """
    Replace multiple sequential slashes (//) with a single slash (/).
    """
    return '/'.join(segment for segment in file_path.split('/') if segment)

def ensure_single_leading_slash(file_path):
    """
    Ensure that the file path starts with a single leading slash.
    """
    if file_path.startswith('/'):
        return file_path  # Already has a leading slash
    else:
        return '/' + file_path  # Add a leading slash

# Read input from standard input
user_input = input()

# Normalize the file path
result_path = normalize_file_path(user_input)

# Print the final normalized file path
print(result_path)
