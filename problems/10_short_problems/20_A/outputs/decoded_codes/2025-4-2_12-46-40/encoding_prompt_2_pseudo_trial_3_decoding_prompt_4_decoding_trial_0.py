def normalize_file_path():
    # Step 1: Read input from the user
    input_path = input().strip()  # Remove leading and trailing whitespace

    # Step 2: Normalize the path
    # Replace any excessive forward slashes at the beginning with a single forward slash
    if input_path.startswith('/'):
        # Find the index of the first non-slash character
        first_non_slash_index = 0
        while first_non_slash_index < len(input_path) and input_path[first_non_slash_index] == '/':
            first_non_slash_index += 1
        
        # Construct the normalized path
        if first_non_slash_index < len(input_path):  # If there are non-slash characters
            normalized_path = '/' + input_path[first_non_slash_index:]
        else:
            normalized_path = '/'  # Only slashes, normalize to single slash
    else:
        normalized_path = '/' + input_path  # No leading slashes, add one

    # Step 3: Output the clean path
    print(normalized_path)

# Call the function to execute
normalize_file_path()
