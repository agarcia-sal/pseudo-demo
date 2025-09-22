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
    Remove leading slashes from the file path and replace them with a single slash.
    
    Args:
        path (str): The file path from which to remove leading slashes.
    
    Returns:
        str: The modified file path with leading slashes replaced by a single slash.
    """
    while path.startswith('/'):
        path = path[1:]
    return '/' + path  # Ensure at least one leading slash remains


def main():
    # Read input from standard input
    input_path = input()
    
    # Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Remove leading slashes from the normalized file path
    final_path = remove_leading_slashes(normalized_path)

    # Output the final modified file path
    print(final_path)


if __name__ == "__main__":
    main()
