import os
import re

def main():
    # Step 1: Read input from standard input
    input_string = input()

    # Step 2: Normalize the path by removing any redundant separators
    normalized_path = normalize(input_string)

    # Step 3: Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)

    # Step 4: Output the final path
    print(final_path)

def normalize(path: str) -> str:
    """
    Normalize the file path by removing redundant separators and up-level references.
    """
    # Using os.path.normpath to normalize the path
    return os.path.normpath(path)

def remove_leading_slashes(path: str) -> str:
    """
    Return the path ensuring at most one leading slash.
    If the path starts with slashes, only one leading slash is kept.
    """
    if path.startswith('/'):
        # Remove all leading slashes
        path = path.lstrip('/')
        # Return a single leading slash if path is not empty
        return '/' + path if path else ''
    else:
        return path

if __name__ == "__main__":
    main()
