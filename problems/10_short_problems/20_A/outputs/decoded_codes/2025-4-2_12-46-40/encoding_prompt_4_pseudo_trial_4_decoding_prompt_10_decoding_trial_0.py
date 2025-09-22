import os

def normalize_path(input_path):
    """
    Normalize the given file path by removing redundant separators and ensuring
    only one leading slash is present if necessary.
    
    Parameters:
    input_path (str): The file path input from the user.
    
    Returns:
    str: The normalized file path.
    """
    # Normalize the path to ensure it uses the OS specific separators
    normalized_path = os.path.normpath(input_path)
    
    # Replace leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path.lstrip('/')
    
    return cleaned_path

def main():
    # Read a file path input from standard input
    input_path = input()
    
    # Normalize and clean the path
    cleaned_path = normalize_path(input_path)
    
    # Output the cleaned path
    print(cleaned_path)

if __name__ == "__main__":
    main()
