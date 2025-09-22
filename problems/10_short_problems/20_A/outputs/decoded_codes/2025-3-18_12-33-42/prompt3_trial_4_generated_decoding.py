import os
import re

def main():
    # Read input from standard input and trim whitespace
    input_path = get_input_from_standard_input()
    
    # Normalize the input path
    normalized_path = normalize_path(input_path)
    
    # Remove leading slashes from the normalized path
    cleaned_path = remove_leading_slashes(normalized_path)
    
    # Output the cleaned path
    print(cleaned_path)

def get_input_from_standard_input():
    """
    Reads all input from standard input, and trims any leading or trailing whitespace.
    Returns:
        str: The trimmed input path.
    """
    return input().strip()

def normalize_path(path):
    """
    Normalizes the provided path using the os.path.normpath method 
    to remove redundant separators and up-level references.
    
    Args:
        path (str): The path to normalize.
        
    Returns:
        str: The normalized path.
    """
    return os.path.normpath(path)

def remove_leading_slashes(path):
    """
    Removes any leading slashes from the path using a regular expression.
    
    Args:
        path (str): The path to process.
        
    Returns:
        str: The path with leading slashes removed, ensuring at most one leading slash.
    """
    return re.sub(r'^/+', '/', path)

if __name__ == "__main__":
    main()
