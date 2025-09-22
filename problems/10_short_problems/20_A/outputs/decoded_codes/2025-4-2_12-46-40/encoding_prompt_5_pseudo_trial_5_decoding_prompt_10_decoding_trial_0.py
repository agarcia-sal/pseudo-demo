import os

def normalize_file_path():
    # STEP 1: Read the file path from standard input and remove extra spaces
    file_path = input().strip()
    
    # STEP 2: Normalize the file path using system path conventions
    normalized_path = os.path.normpath(file_path)
    
    # STEP 3: Remove leading slashes and ensure a single leading slash
    final_path = normalized_path.lstrip('/').replace('//', '/')  # Replace multiple leading slashes
    if final_path and not final_path.startswith('/'):
        final_path = '/' + final_path  # Ensure there's a leading slash
    
    # STEP 4: Output the result
    print(final_path)

# If needed, this function can be called
# normalize_file_path()
