def normalize_file_path_and_print(input_string):
    # REMOVE leading and trailing whitespace from input_string
    cleaned_input = input_string.strip()
    
    # NORMALIZE the file path using a standard format
    # (Assuming normalization means converting to an absolute path,
    # for simplicity we'll represent this with a placeholder function)
    normalized_path = normalize_path(cleaned_input)
    
    # REPLACE any occurrences of multiple leading slashes with a single leading slash
    formatted_path = replace_multiple_leading_slashes(normalized_path)
    
    # PRINT the formatted file path
    print(formatted_path)

def normalize_path(path):
    # Placeholder for actual normalization logic
    # For demonstration purposes, just returning the path as is
    return path

def replace_multiple_leading_slashes(path):
    while path.startswith("//"):
        path = path[1:]  # Remove one leading slash
    return path

# MAIN EXECUTION BLOCK
input_string = input()  # Read input from standard input
normalize_file_path_and_print(input_string)
