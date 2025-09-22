import os

def normalize_file_path():
    # Step 1: Get Input
    file_path = input().strip()

    # Step 2: Normalize the Path
    normalized_path = os.path.normpath(file_path)

    # Step 3: Ensure Proper Format
    # Remove leading slashes and keep only one
    if normalized_path.startswith('/'):
        # Strip leading slashes and add a single leading slash
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path
    
    # Step 4: Display Result
    print(normalized_path)

# Call the function to execute the normalization
normalize_file_path()
