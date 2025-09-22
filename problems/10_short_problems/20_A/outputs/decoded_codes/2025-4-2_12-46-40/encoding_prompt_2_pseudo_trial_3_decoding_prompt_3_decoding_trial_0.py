def normalize_file_path():
    # Step 1: Read the input file path and strip surrounding whitespace
    input_path = input().strip()
    
    # Step 2: Normalize the path by replacing multiple slashes at the start with one
    if input_path.startswith('/'):
        # Find the index of the first non-slash character
        first_non_slash_index = 0
        while first_non_slash_index < len(input_path) and input_path[first_non_slash_index] == '/':
            first_non_slash_index += 1
            
        # Normalize leading slashes to a single slash
        normalized_path = '/' + input_path[first_non_slash_index:]
    else:
        # If there are no leading slashes, just use the input as-is
        normalized_path = input_path
    
    # Step 3: Print the cleaned-up path
    print(normalized_path)

# Example usage
normalize_file_path()
