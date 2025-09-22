import os

def normalize_file_path(file_path: str) -> str:
    """
    Normalize the given file path by resolving redundant separators,
    and ensuring it starts with a single slash if applicable.
    
    Args:
        file_path (str): The input file path to normalize.
        
    Returns:
        str: The normalized file path.
    """
    # Use os.path.normpath to normalize the file path
    normalized_path = os.path.normpath(file_path)

    # Remove leading slashes
    if normalized_path.startswith('/'):
        normalized_path = normalized_path.lstrip('/')
    
    # Ensure the output starts with a single slash
    return '/' + normalized_path

def main():
    # Step 1: Read input
    user_input_path = input()
    
    # Step 2 and 3: Normalize the file path and remove leading slashes
    final_path = normalize_file_path(user_input_path)
    
    # Step 4: Output the resulting path
    print(final_path)

# Using the main block to encapsulate executable code
if __name__ == "__main__":
    main()
