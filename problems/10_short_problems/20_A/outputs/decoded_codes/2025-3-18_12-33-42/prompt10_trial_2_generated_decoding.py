import re

def main():
    # Read input from standard input and trim whitespace
    input_string = read_input()
    
    # Normalize the path by removing redundant separators
    normalized_path = normalize_path(input_string)
    
    # Replace multiple leading slashes with a single slash
    final_path = replace_leading_slashes(normalized_path)

    # Output the final normalized path
    print(final_path)

def normalize_path(path):
    """Normalize the path by removing redundant separators."""
    return remove_redundant_separators(path)

def remove_redundant_separators(path):
    """Remove redundant separators from the path."""
    # Replace occurrences of '//' with '/' until no more are found
    while '//' in path:
        path = path.replace('//', '/')
    return path

def replace_leading_slashes(path):
    """Replace leading slashes with a single slash."""
    return re.sub(r'^/+', '/', path)

def read_input():
    """Read input from the user and trim whitespace."""
    return input().strip()

if __name__ == "__main__":
    main()
