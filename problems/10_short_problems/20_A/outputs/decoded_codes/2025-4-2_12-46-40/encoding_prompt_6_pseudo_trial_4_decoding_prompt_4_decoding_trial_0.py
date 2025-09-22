def main():
    # Step 1: Read input from the user
    user_input = input()

    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)

    # Step 3: Adjust leading slashes
    if normalized_path.startswith("/"):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)

    # Step 4: Output the final normalized path
    print(normalized_path)


def normalize_path(input_path: str) -> str:
    """
    Normalize the given file path by removing redundant elements like
    '.' and '..', and ensuring a standard format.
    
    Returns the normalized path as a string.
    """
    # The os module provides a method to normalize paths
    import os
    # os.path.normpath() normalizes the path
    return os.path.normpath(input_path)


def replace_multiple_leading_slashes_with_one(path: str) -> str:
    """
    Replace multiple leading slashes in the path with a single slash.
    
    Returns the modified path.
    """
    while path.startswith("//"):
        path = path[1:]  # Remove the first slash
    return path


if __name__ == "__main__":
    main()
