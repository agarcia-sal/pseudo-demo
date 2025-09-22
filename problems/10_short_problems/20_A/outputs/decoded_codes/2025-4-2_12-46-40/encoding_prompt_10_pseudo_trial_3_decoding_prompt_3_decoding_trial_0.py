import os

def main():
    # Read input string from standard input
    input_string = input()

    # Normalize the path by removing any redundant separators
    normalized_path = normalize(input_string)

    # Remove leading slashes from the normalized path, ensuring at most one leading slash remains
    final_path = remove_leading_slashes(normalized_path)

    # Output the final path
    print(final_path)

def normalize(path):
    """
    Normalize the file path by removing redundant separators and up-level references.
    This uses os.path.normpath as the actual implementation.
    """
    return os.path.normpath(path)

def remove_leading_slashes(path):
    """
    Remove leading slashes from the path, ensuring at most one leading slash remains.
    If the path is empty after removing slashes, return an empty string.
    """
    if path.startswith('/'):
        # Remove leading slashes
        path = path.lstrip('/')
        # If the path is not empty, return a single leading slash + rest
        if path:
            return '/' + path
        else:
            return ''  # Return empty string if no path remains
    else:
        return path  # Return original path if it doesn't start with a slash

if __name__ == "__main__":
    main()
