import re

def normalize_and_print_path():
    # Read input from standard input
    raw_input = input()
    
    # Normalize the input path
    normalized_path = normalize_path(raw_input)
    
    # Print the modified path, replacing multiple leading slashes with a single slash
    print(replace_leading_slashes(normalized_path))

def normalize_path(raw_input):
    # Remove any leading or trailing whitespace from the input
    trimmed_input = raw_input.strip()
    
    # Normalize the file path (placeholder for actual normalization logic)
    normalized_path = standard_path_normalization(trimmed_input)
    
    return normalized_path

def replace_leading_slashes(path):
    # Use a regular expression to replace multiple leading slashes with a single slash
    modified_path = re.sub(r'^/+', '/', path)
    
    return modified_path

def standard_path_normalization(path):
    # Placeholder function for actual path normalization logic
    # In a real implementation, you would resolve '.', '..' and combine paths properly
    return path

# Trigger the normalization and print function
normalize_and_print_path()
