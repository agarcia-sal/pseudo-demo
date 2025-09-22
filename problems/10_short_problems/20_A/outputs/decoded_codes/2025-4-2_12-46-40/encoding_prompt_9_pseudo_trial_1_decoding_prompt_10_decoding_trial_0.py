import os

def normalize_path(path):
    """
    Normalize the given file path by removing unnecessary segments
    and ensuring it starts with a single leading slash.
    
    Parameters:
    - path (str): The input file path to normalize.

    Returns:
    - str: The normalized file path.
    """
    # Remove leading and trailing spaces
    cleaned_path = path.strip()
    
    # Normalize the path using os.path.normpath to remove redundant segments
    normalized_path = os.path.normpath(cleaned_path)
    
    # Ensure the path starts with a single leading slash if necessary
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path
    
    return normalized_path

def main():
    """
    Main function to execute the program logic, capturing user input,
    normalizing the path and printing the result.
    """
    # Read input from the user
    user_input = input()
    
    # Normalize the given path
    result_path = normalize_path(user_input)
    
    # Output the result
    print(result_path)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
