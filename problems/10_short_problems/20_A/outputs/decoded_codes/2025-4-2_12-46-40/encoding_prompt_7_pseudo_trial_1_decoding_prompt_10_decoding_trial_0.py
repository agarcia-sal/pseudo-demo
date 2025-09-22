import os

def normalize(input_path):
    """
    Normalize the file path by converting it to a standard format.
    This function removes extraneous components like '..' and '.' in the path.
    
    Args:
    - input_path (str): The raw file path to be normalized.
    
    Returns:
    - str: The normalized file path.
    """
    # Use os.path.normpath to standardize the path
    return os.path.normpath(input_path)

def normalize_and_print_path():
    """
    Read a file path from the user input, normalize it, and print the final formatted path.
    The function ensures that leading slashes are trimmed down to a single leading slash.
    """
    # Read input from standard input and strip leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        # Replace any occurrences of multiple leading slashes
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')

    # Output the final formatted path
    print(final_path)

# You can call the function here to execute the program
if __name__ == "__main__":
    normalize_and_print_path()
