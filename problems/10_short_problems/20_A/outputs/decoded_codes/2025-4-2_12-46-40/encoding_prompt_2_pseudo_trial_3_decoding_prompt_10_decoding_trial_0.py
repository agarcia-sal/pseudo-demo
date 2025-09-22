def normalize_file_path(file_path):
    """
    Normalizes the file path by removing unnecessary slashes
    and ensuring it starts with a single forward slash.

    :param file_path: The original file path input as a string
    :return: A cleaned-up file path string
    """
    # Step 1: Strip leading and trailing whitespace from the input path
    stripped_path = file_path.strip()
    
    # Step 2: Normalize the path by replacing multiple leading slashes with a single slash
    if stripped_path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        normalized_path = '/' + stripped_path.lstrip('/')
    else:
        normalized_path = stripped_path
    
    return normalized_path

def main():
    # Step 3: Read input from the user
    file_path = input()
    
    # Step 4: Normalize the file path
    cleaned_path = normalize_file_path(file_path)
    
    # Step 5: Output the cleaned file path
    print(cleaned_path)

if __name__ == "__main__":
    main()
