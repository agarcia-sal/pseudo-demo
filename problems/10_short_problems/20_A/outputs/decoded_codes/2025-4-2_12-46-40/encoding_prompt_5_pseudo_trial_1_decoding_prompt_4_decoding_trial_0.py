import os

def read_input():
    """
    Read input from user and remove excess whitespace.
    Returns the cleaned path as a string.
    """
    input_path = input().strip()  # Get user input and strip spaces
    return input_path

def normalize_path(path):
    """
    Normalize the file path by removing redundant separators
    and up-level references. This utilizes `os.path.normpath`
    for path normalization.
    """
    normalized_path = os.path.normpath(path)  # Normalize the path
    return normalized_path

def ensure_single_leading_slash(path):
    """
    Ensure the path starts with a single forward slash.
    Converts multiple leading slashes to a single one.
    """
    if path.startswith('/'):
        adjusted_path = '/' + path.lstrip('/')  # Replace leading slashes with a single slash
    else:
        adjusted_path = path  # Return the path as is if it has no leading slash
    
    return adjusted_path

def main():
    """
    Main execution flow that orchestrates the reading,
    normalizing, and outputting of the cleaned file path.
    """
    user_input = read_input()  # Read and clean the input path
    normalized_input = normalize_path(user_input)  # Normalize the input path
    final_path = ensure_single_leading_slash(normalized_input)  # Ensure single leading slash
    
    print(final_path)  # Output the final cleaned path

if __name__ == "__main__":
    main()  # Call the main function to execute the program
