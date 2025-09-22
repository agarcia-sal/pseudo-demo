import os

def normalize_file_path():
    # Step 1: Read the input file path from the user
    input_path = input()
    
    # Step 2: Normalize the path to POSIX format
    # Using os.path.normpath to normalize the path and replace backslashes on Windows
    normalized_path = os.path.normpath(input_path).replace("\\", "/")
    
    # Step 3: Remove leading slashes
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')

    # Step 4: Print the resulting path
    print(final_path)

# Main execution
normalize_file_path()
