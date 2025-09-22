def normalize_file_path():
    # Step 1: Read the input file path and strip whitespace
    raw_file_path = input()
    normalized_path = raw_file_path.strip()
    
    # Step 2: Normalize the path
    # Replace multiple leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        # Remove leading slashes
        normalized_path = normalized_path.lstrip('/')  # Remove all leading slashes
        normalized_path = '/' + normalized_path  # Add a single leading slash

    # Step 3: Print the normalized file path
    print(normalized_path)

# Example test case
# Input: '//user//documents//file.txt'
# Expected Output: '/user/documents/file.txt'
