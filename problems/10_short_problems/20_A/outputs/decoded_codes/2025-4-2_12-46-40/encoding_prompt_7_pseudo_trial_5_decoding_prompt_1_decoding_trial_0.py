def normalize_file_path_and_print(input_string):
    # REMOVE leading and trailing whitespace from inputString
    cleaned_input = input_string.strip()
    
    # NORMALIZE the file path using a standard format
    normalized_path = normalize_path(cleaned_input)
    
    # REPLACE any occurrences of multiple leading slashes with a single leading slash
    formatted_path = replace_multiple_leading_slashes(normalized_path)
    
    # PRINT the formatted file path
    print(formatted_path)

# Function to normalize the path (assuming some standard normalization logic)
def normalize_path(path):
    # Placeholder for normalization logic; replace with actual logic
    return path  # This would normally include actual normalization logic

# Function to replace multiple leading slashes with a single slash
def replace_multiple_leading_slashes(path):
    while path.startswith('//'):
        path = path.replace('//', '/', 1)
    return path

# MAIN EXECUTION BLOCK
input_string = input()
normalize_file_path_and_print(input_string)
