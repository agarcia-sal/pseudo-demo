import os

def transform_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_string = input()
    trimmed_input_string = input_string.strip()
    
    # Normalize the path to a standard format
    normalized_path = os.path.normpath(trimmed_input_string)
    
    # Replace sequences of leading slashes with a single slash
    if normalized_path.startswith('/'):
        updated_path = '/' + normalized_path.lstrip('/')
    else:
        updated_path = normalized_path.lstrip('/')
    
    # Output the final transformed path
    print(updated_path)

# Execute the function
transform_path()
