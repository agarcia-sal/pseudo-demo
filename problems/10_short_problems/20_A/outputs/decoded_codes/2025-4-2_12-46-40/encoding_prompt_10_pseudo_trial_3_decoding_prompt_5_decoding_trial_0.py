import os

def main():
    # Read input string from standard input
    input_string = input()
    
    # Normalize the path by removing any redundant separators
    normalized_path = normalize(input_string)
    
    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final path
    print(final_path)

def normalize(path):
    """
    This function normalizes the file path.
    The implementation uses os.path.normpath to remove extraneous separators.
    """
    return os.path.normpath(path)

def remove_leading_slashes(path):
    """
    This function returns the path with at most one leading slash.
    If the path starts with slashes, we remove them and return a single leading slash if the path is not empty.
    """
    if path.startswith('/'):  # Check if the path starts with a slash
        # Remove leading slashes
        path = path.lstrip('/')
        # If the path is not empty after removing slashes, prepend a single slash
        if path:
            return '/' + path
        else:
            return ''  # Return empty string if no remaining path
    else:
        return path  # Return path unchanged if it doesn't start with a slash

if __name__ == "__main__":
    main()
