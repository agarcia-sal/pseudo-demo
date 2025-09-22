import os

def read_input():
    """Reads input from standard input and trims whitespace."""
    return input().strip()

def normalize_path(path):
    """Normalizes the file path to eliminate redundant separators and up-level references."""
    return os.path.normpath(path)

def adjust_leading_slashes(path):
    """Ensures the path starts with a single forward slash."""
    # Remove all leading slashes, then add a single leading slash
    return '/' + path.lstrip('/')

def main():
    # Step 1: Read input
    original_path = read_input()
    
    # Step 2: Normalize the file path
    normalized_path = normalize_path(original_path)
    
    # Step 3: Ensure the path starts with a single forward slash
    final_path = adjust_leading_slashes(normalized_path)
    
    # Step 4: Output the final result
    print(final_path)

if __name__ == "__main__":
    main()
