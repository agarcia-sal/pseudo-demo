def normalize_file_path_and_print(input_string):
    # REMOVE leading and trailing whitespace from input_string
    cleaned_input = input_string.strip()
    
    # NORMALIZE the file path using a standard format
    # Assuming normalization means using a standard format for slashes
    normalized_path = cleaned_input.replace('\\', '/')
    
    # REPLACE any occurrences of multiple leading slashes with a single leading slash
    while '//' in normalized_path[:2]:  # Check only the leading part
        normalized_path = normalized_path.replace('//', '/')
    
    # PRINT the formatted file path
    print(normalized_path)

# MAIN EXECUTION BLOCK
input_string = input()
normalize_file_path_and_print(input_string)
