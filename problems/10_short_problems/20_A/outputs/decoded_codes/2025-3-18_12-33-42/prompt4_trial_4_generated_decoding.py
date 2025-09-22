import os

def normalize_path(path):
    # Normalize the path to ensure no redundant separators
    normalized_path = os.path.normpath(path)
    return normalized_path

def replace_leading_slashes(path):
    # Replace multiple leading slashes with a single leading slash
    if path.startswith('/'):
        # Strip leading slashes
        path = path.lstrip('/')
        # Add a single slash at the start
        path = '/' + path
    return path

def main():
    # Read input from standard input
    input_string = input()
    
    # Normalize the file path to remove redundant separators
    normalized_path = normalize_path(input_string)
    
    # Replace multiple leading slashes with a single slash in normalized_path
    result_path = replace_leading_slashes(normalized_path)

    # Output the final result
    print(result_path)

# Ensure the main function runs when executing the script
if __name__ == "__main__":
    main()
