def normalize_path(path):
    """
    Normalize the file path by converting backslashes to forward slashes.
    
    Args:
        path (str): The original file path.
    
    Returns:
        str: The normalized file path.
    """
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    """
    Remove leading slashes from the path and ensure only one leading slash remains.
    
    Args:
        path (str): The normalized file path.
    
    Returns:
        str: The final path with at most one leading slash.
    """
    return '/' + path.lstrip('/')

def main():
    # Read input for the file path
    input_path = input()
    
    # Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Remove leading slashes from the normalized file path
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final modified file path
    print(final_path)

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
