import os

def main():
    # Step 1: Read user input for the file path
    user_input = input()
    
    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Adjust leading slashes to ensure only one exists
    if normalized_path.startswith("/"):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)
    
    # Step 4: Output the final normalized path
    print(normalized_path)

def normalize_path(input_path: str) -> str:
    """
    Normalize the given file path to ensure it has a standard format.
    
    :param input_path: The original file path provided by the user.
    :return: A normalized version of the input file path.
    """
    # Use os.path.normpath to normalize the path (handles '..' and '.')
    return os.path.normpath(input_path)

def replace_multiple_leading_slashes_with_one(path: str) -> str:
    """
    Replace multiple leading slashes in the path with a single slash.
    
    :param path: The file path potentially containing multiple leading slashes.
    :return: The path with leading slashes replaced by a single "/".
    """
    # Use regex to replace multiple leading slashes with a single slash
    return '/' + path.lstrip('/')

if __name__ == "__main__":
    main()
