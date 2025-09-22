import os

def process_path():
    # Read input path from standard input
    input_path = input()
    
    # Normalize the input path using POSIX standards
    normalized_path = os.path.normpath(input_path)
    
    # Remove leading slashes, ensuring at least one leading slash remains
    if normalized_path.startswith('/'):
        # Replace leading slashes with one leading slash
        result_path = '/' + normalized_path.lstrip('/')
    else:
        # If it doesn't start with a slash, return the path as is
        result_path = normalized_path
    
    # Output the final processed path
    print(result_path)

# Execute the function to process the path
process_path()
