def normalize_path(path):
    """
    Normalize the file path by replacing backslashes with forward slashes.
    
    Args:
        path (str): The file path to normalize.
    
    Returns:
        str: The normalized file path with forward slashes.
    """
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    """
    Remove leading slashes from the path, replacing them with a single slash.
    
    Args:
        path (str): The file path to process.
    
    Returns:
        str: The path with leading slashes removed or replaced by a single slash.
    """
    # Strip leading slashes and then add a leading slash if the result is not empty
    return '/' + path.lstrip('/')

def main():
    # Read input from standard input (stdin)
    input_path = input()
    
    # Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Remove leading slashes from the normalized file path
    final_path = remove_leading_slashes(normalized_path)

    # Output the final modified file path
    print(final_path)

if __name__ == "__main__":
    main()
