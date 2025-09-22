import re
import posixpath

def normalize_file_path():
    # Step 1.1: Read the input file path from the user
    file_path = input()

    # Step 1.2: Normalize the path to eliminate redundant slashes
    normalized_path = posixpath.normpath(file_path)

    # Step 1.3: Ensure the path starts with exactly one forward slash
    # Replace multiple leading slashes with a single forward slash
    if normalized_path.startswith('/'):
        modified_path = re.sub(r'^(//+)', '/', normalized_path)
    else:
        modified_path = '/' + normalized_path
    
    # Step 1.4: Output the modified path to the user
    print(modified_path)

# Call the function to execute the normalization process
normalize_file_path()
