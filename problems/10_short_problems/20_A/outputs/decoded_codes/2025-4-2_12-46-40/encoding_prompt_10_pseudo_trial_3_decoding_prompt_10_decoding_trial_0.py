import re

def normalize(path: str) -> str:
    """Normalize the file path by removing redundant separators."""
    # This uses a regular expression to replace multiple consecutive slashes with a single slash
    return re.sub(r'/+', '/', path)

def remove_leading_slashes(path: str) -> str:
    """Remove leading slashes from the path, ensuring at most one leading slash remains."""
    if path.startswith('/'):
        # Remove all leading slashes
        path = path.lstrip('/')
        # If the path is not empty after removing leading slashes, return a single leading slash
        if path:
            return '/' + path
        else:
            return ''  # Return empty string if path was only slashes
    else:
        return path  # Return the path as is if it doesn't start with a slash

def main():
    # Read input path from standard input
    input_string = input()
    
    # Normalize the path by removing redundant separators
    normalized_path = normalize(input_string)
    
    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final path
    print(final_path)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
