import os

def normalize_file_path(file_path: str) -> str:
    """
    Normalize the given file path by removing redundant separators
    and up-level references. It also ensures that the path starts
    with a single leading slash if it originally had one or more.
    
    Args:
        file_path (str): The file path to normalize.
    
    Returns:
        str: The normalized file path.
    """
    # Step 1: Trim leading and trailing whitespace
    trimmed_path = file_path.strip()
    
    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(trimmed_path)
    
    # Step 3: Adjust leading slashes
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    return normalized_path

def main():
    # Step 1: Read input
    file_path_input = input()
    
    # Step 2: Normalize the file path
    normalized_path = normalize_file_path(file_path_input)
    
    # Step 3: Output the final adjusted file path
    print(normalized_path)

# Run the program if this script is executed
if __name__ == "__main__":
    main()
