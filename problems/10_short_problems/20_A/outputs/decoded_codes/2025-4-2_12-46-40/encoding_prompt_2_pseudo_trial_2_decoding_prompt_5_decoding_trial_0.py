import os

def normalize_file_path():
    # Read input from the user
    file_path = input()
    
    # Remove leading and trailing whitespace
    normalized_path = file_path.strip()
    
    # Normalize the file path to resolve relative components
    normalized_path = os.path.normpath(normalized_path)
    
    # Adjust path format to start with a single forward slash
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Display the modified file path
    print(normalized_path)

# Example test cases (uncomment to run)
# Input: "  ../user/../documents/file.txt  "
# Expected output: "/user/documents/file.txt"
# normalize_file_path()
