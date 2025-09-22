def normalize_file_path_and_print(input_string):
    # REMOVE leading and trailing whitespace from input_string
    cleaned_input = input_string.strip()
    
    # NORMALIZE the file path using a standard format
    normalized_path = cleaned_input  # Placeholder for normalization logic
    
    # REPLACE any occurrences of multiple leading slashes with a single leading slash
    if normalized_path.startswith('//'):
        formatted_path = '/' + normalized_path.lstrip('/')
    else:
        formatted_path = normalized_path
    
    # PRINT the formatted file path
    print(formatted_path)

# MAIN EXECUTION BLOCK
input_string = input()  # Read input from standard input
normalize_file_path_and_print(input_string)
