import os

def normalize_path(input_path: str) -> str:
    """
    Normalize the given file path.
    
    This function removes any redundant elements in the file path 
    and returns the normalized version of the input path.
    """
    # Use os.path.normpath to normalize the path
    normalized_path = os.path.normpath(input_path)
    return normalized_path

def replace_multiple_leading_slashes_with_one(path: str) -> str:
    """
    Replace multiple leading slashes in the path with a single slash.

    Args:
        path (str): The file path that may have multiple leading slashes.
        
    Returns:
        str: The modified path with leading slashes replaced.
    """
    # Using lstrip to remove leading slashes and then adding back one slash
    return '/' + path.lstrip('/')

def main():
    """
    Main function to read input and display the normalized file path.
    """
    # Step 1: Read input from the user
    user_input = input()
    
    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Adjust leading slashes if necessary
    if normalized_path.startswith('/'):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)
    
    # Step 4: Output the final normalized path
    print(normalized_path)

if __name__ == "__main__":
    main()
