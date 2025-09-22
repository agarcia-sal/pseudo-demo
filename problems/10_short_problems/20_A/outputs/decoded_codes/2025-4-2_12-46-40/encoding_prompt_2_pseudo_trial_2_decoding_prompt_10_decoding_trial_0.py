import os

def normalize_file_path():
    # Step 1: Read a line of input from the user
    file_path = input()
    
    # Step 2: Remove any leading or trailing whitespace from the input
    file_path = file_path.strip()
    
    # Step 3: Normalize the file path by resolving relative components
    # This will convert ".." and "." to standard path format
    normalized_path = os.path.normpath(file_path)
    
    # Step 4: Adjust path format - replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Step 5: Display the modified file path to the user
    print(normalized_path)

# Invoke the function
normalize_file_path()
