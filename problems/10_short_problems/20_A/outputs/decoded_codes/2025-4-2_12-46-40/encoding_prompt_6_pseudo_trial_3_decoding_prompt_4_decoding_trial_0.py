import os

def normalize_path(input_string):
    # Read input from standard input and remove leading/trailing whitespace
    trimmed_input_string = input_string.strip()
    
    # Normalize the path to a standard format using os.path.normpath
    normalized_path = os.path.normpath(trimmed_input_string)
    
    # Replace leading slashes with a single slash
    if normalized_path.startswith('/'):
        updated_path = '/' + normalized_path.lstrip('/')
    else:
        updated_path = normalized_path.lstrip('/')

    # Output the final transformed path
    print(updated_path)

# Assume input will be provided through standard input
user_input = input()
normalize_path(user_input)
