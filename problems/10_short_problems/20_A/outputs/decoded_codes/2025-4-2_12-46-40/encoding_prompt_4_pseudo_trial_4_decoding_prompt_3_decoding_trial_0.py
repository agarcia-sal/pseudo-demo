import os

def get_cleaned_path():
    # Read a file path input from standard input
    input_path = input().strip()  # Read and strip any surrounding whitespace

    # Normalize the file path by using os.path.normpath to remove redundant separators
    normalized_path = os.path.normpath(input_path)

    # Replace any leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path.lstrip('/')

    # Output the cleaned path
    print(cleaned_path)

# Execute the function
get_cleaned_path()
