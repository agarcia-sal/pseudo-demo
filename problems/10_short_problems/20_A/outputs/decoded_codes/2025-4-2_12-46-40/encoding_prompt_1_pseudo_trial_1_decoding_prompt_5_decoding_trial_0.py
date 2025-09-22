import os

def normalize_file_path():
    # Read a file path from standard input
    file_path = input()
    
    # Remove extra whitespace from the beginning and end of the input string
    file_path = file_path.strip()
    
    # Normalize the file path
    normalized_path = os.path.normpath(file_path)
    
    # Adjust leading slashes to a single slash
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Output the final adjusted file path
    print(normalized_path)

# Call the function to execute it
normalize_file_path()
