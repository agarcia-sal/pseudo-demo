import os

def normalize_path():
    # Read input from the user
    user_input = input()
    
    # Remove leading and trailing whitespace from the input
    trimmed_input = user_input.strip()
    
    # Normalize the path by eliminating redundant separators and up-level references
    normalized_path = os.path.normpath(trimmed_input)
    
    # Replace multiple leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')
    
    # Output the final normalized path
    print(final_path)

# Call the function to execute the code
normalize_path()
