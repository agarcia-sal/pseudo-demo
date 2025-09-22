import os

def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = os.path.normpath(input_path)
    
    # Replace any leading slashes with a single slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]
    formatted_path = '/' + normalized_path
    
    # Output the formatted path
    print(formatted_path)
