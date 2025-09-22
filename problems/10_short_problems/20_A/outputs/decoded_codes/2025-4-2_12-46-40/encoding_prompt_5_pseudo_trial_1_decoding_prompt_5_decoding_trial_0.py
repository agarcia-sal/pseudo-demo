def read_input():
    # Get the path from standard input and remove excess whitespace
    input_path = input().strip()
    return input_path

def normalize_path(path):
    # Normalize the file path by removing redundant separators and up-level references
    normalized_path = path.replace('//', '/').replace('/./', '/').replace('/../', '/').rstrip('/')
    while '/../' in normalized_path:
        normalized_path = normalized_path.replace('/../', '/')
    return normalized_path

def ensure_single_leading_slash(path):
    # If the path starts with one or more slashes
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjusted_path = path.lstrip('/')
        return '/' + adjusted_path
    else:
        # Return the path as is since it already has a single slash
        return path

def main():
    # Read and clean the input path
    user_input = read_input()
    
    # Normalize the input path for standardization
    normalized_input = normalize_path(user_input)
    
    # Ensure the normalized path has a proper leading slash
    final_path = ensure_single_leading_slash(normalized_input)
    
    # Output the final cleaned path
    print(final_path)

# Start the program execution
main()
