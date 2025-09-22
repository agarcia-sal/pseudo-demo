def normalize_path(path):
    """
    Normalize the file path by replacing multiple consecutive slashes with a single slash.
    
    Args:
    path (str): The original file path input.
    
    Returns:
    str: The normalized file path.
    """
    while '//' in path:
        path = path.replace('//', '/')
    return path

def format_path(path):
    """
    Format the file path to ensure it starts with a single slash.
    
    Args:
    path (str): The normalized file path.
    
    Returns:
    str: The formatted file path that starts with a single slash.
    """
    if path.startswith('/'):
        return path
    return '/' + path

def main():
    """
    Main function to read a file path from input, normalize it, and print the formatted result.
    """
    input_path = input()  # Read input from standard input
    normalized_path = normalize_path(input_path)  # Normalize the input path
    print(format_path(normalized_path))  # Print the formatted path

if __name__ == "__main__":
    main()
