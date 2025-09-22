import re

def normalize(path):
    """
    This function normalizes the file path by removing redundant separators.
    It preserves a clean format for paths.
    Assumes that double slashes (//) or trailing slashes should be reduced.
    """
    # Replace multiple consecutive slashes with a single slash
    path = re.sub(r'/+', '/', path)
    # Return normalized path without leading/trailing slashes
    return path.strip('/')

def remove_leading_slashes(path):
    """
    This function ensures that the path has at most one leading slash.
    If the input path is empty or only contains slashes, it returns an empty string.
    """
    # If path starts with one or more slashes
    if path.startswith('/'):
        # Remove leading slashes
        path = path.lstrip('/')
        # If the path is not empty after removing slashes
        if path:
            # Return with a single leading slash
            return '/' + path
        else:
            # Return empty string if the path is empty
            return ''
    else:
        # If the path does not start with a slash, return it as is
        return path

# Main logic
if __name__ == "__main__":
    # Read input from standard input
    input_string = input()
    
    # Normalize the path
    normalized_path = normalize(input_string)
    
    # Remove leading slashes to generate the final path
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final path
    print(final_path)
