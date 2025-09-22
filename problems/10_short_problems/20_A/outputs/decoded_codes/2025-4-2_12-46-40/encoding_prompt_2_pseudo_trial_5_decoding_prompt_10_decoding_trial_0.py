import os

def normalize_path(input_path):
    """
    Normalize the given file path and ensure it has a single leading slash.
    
    Parameters:
    input_path (str): The input file path to normalize.
    
    Returns:
    str: The normalized file path with a single leading slash.
    """
    # Remove leading and trailing whitespace
    cleaned_path = input_path.strip()
    
    # Normalize the path using os.path.normpath
    normalized_path = os.path.normpath(cleaned_path)
    
    # Modify leading slashes
    if normalized_path.startswith("/"):
        # Replace multiple leading slashes with a single slash
        normalized_path = "/" + normalized_path.lstrip("/")
    
    return normalized_path

def main():
    # Read input from standard input
    user_input = input()
    
    # Normalize the path and get the result
    result_path = normalize_path(user_input)
    
    # Output the modified path
    print(result_path)

if __name__ == "__main__":
    main()
