def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = input_path.replace('//', '/').replace('\\', '/')  # Windows and Unix separators
    while '//' in normalized_path:
        normalized_path = normalized_path.replace('//', '/')
    
    # Replace any leading slashes with a single slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]
    formatted_path = '/' + normalized_path
    
    # Output the formatted path
    print(formatted_path)

# This function can then be tested with various inputs.
# Example test cases:
# Input: "////user///documents//file.txt"
# Expected Output: "/user/documents/file.txt"
