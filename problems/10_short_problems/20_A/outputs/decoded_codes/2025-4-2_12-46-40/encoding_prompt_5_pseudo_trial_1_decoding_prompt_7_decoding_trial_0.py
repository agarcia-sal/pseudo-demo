def read_input():
    # Get the path from standard input and remove excess whitespace
    input_path = input().strip()  # Read input and trim spaces
    return input_path

def normalize_path(path):
    # Normalize the file path to remove any redundant separators and up-level references
    # This implementation uses Python's os.path library for normalization
    import os
    normalized_path = os.path.normpath(path)  # Normalize the path
    return normalized_path

def ensure_single_leading_slash(path):
    # If the path starts with one or more slashes
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjusted_path = '/' + path.lstrip('/')  # Keep a single leading slash
    else:
        # Return the path as is since it already has a single slash
        adjusted_path = path
    
    return adjusted_path

def main():
    # Read and clean the input path
    user_input = read_input()
    
    # Normalize the input path for standardization
    normalized_input = normalize_path(user_input)
    
    # Ensure the normalized path has a proper leading slash
    final_path = ensure_single_leading_slash(normalized_input)
    
    # Output the final cleaned path
    print(final_path)

# Execute the main function
main()
