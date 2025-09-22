import os

def normalize_path():
    # Read input from the user
    user_input = input()
    
    # Remove leading and trailing whitespace from the input
    trimmed_input = user_input.strip()
    
    # Normalize the path by eliminating redundant separators and up-level references
    normalized_path = os.path.normpath(trimmed_input)
    
    # Replace multiple leading slashes with a single leading slash
    # This uses regex to replace any series of leading slashes with a single slash
    final_path = normalized_path.lstrip('/').rjust(len(normalized_path), '/')
    
    # Output the final normalized path
    print(final_path)

# To run the function, uncomment the following line:
# normalize_path()
