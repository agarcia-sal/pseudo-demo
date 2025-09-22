import os
import re

def normalize_file_path():
    # Read input from the user
    user_input = input()
    
    # Remove leading and trailing whitespace from the input
    trimmed_input = user_input.strip()
    
    # Normalize the path by eliminating redundant separators and up-level references
    normalized_path = os.path.normpath(trimmed_input)
    
    # Replace multiple leading slashes with a single leading slash
    final_path = re.sub(r'^(/{2,})', '/', normalized_path)
    
    # Output the final normalized path
    print(final_path)

# Call the function to execute the normalization
normalize_file_path()
