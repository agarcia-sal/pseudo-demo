import re
import os

def normalize_path(input_string):
    """
    Normalize the path by removing redundant separators and up-level references.
    
    Args:
    input_string (str): The input path as a string.
    
    Returns:
    str: The normalized path.
    """
    return os.path.normpath(input_string)

def substitute_leading_slashes(path):
    """
    Replace leading slashes in the path with a single slash.
    
    Args:
    path (str): The input path as a string.
    
    Returns:
    str: The processed path with leading slashes modified.
    """
    # Replace multiple leading slashes with a single slash
    return re.sub(r'^/{2,}', '/', path)

def main():
    # Read input from standard input and trim leading and trailing whitespace
    input_string = input().strip()
    
    # Normalize the input path
    normalized_path = normalize_path(input_string)
    
    # Substitute leading slashes with a single slash
    result_path = substitute_leading_slashes(normalized_path)
    
    # Print the final result path
    print(result_path)

if __name__ == "__main__":
    main()
