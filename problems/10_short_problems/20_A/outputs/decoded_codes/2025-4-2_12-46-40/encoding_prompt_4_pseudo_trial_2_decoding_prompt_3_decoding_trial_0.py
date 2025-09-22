import os

def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = os.path.normpath(input_path)
    
    # Replace any leading slashes with a single slash
    formatted_path = normalized_path.lstrip('/').rfind('/') + 1
    
    # Output the formatted path, ensuring it begins with a single /
    if formatted_path > 0:
        formatted_path = '/' + normalized_path[formatted_path:]
    else:
        formatted_path = '/' + normalized_path
    
    print(formatted_path)

# Example usage: Uncomment the line below to run the function
# normalize_and_format_path()
