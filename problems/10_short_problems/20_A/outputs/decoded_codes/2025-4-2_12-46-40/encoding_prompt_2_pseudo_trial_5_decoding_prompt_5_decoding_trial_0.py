import os

def normalize_and_format_path():
    # Step 1: Read input and remove leading/trailing whitespace
    user_input = input().strip()
    
    # Step 2: Normalize the input path to a standard format
    normalized_path = os.path.normpath(user_input)
    
    # Step 3: Modify leading slashes to ensure only one forward slash at the beginning
    if normalized_path.startswith('/'):
        # Replace multiple leading slashes with a single forward slash
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Step 4: Output the modified path
    print(normalized_path)

# Example test cases to consider:
# Input: "///user//documents//file.txt" should output: "/user/documents/file.txt"
# Input: "user//documents//../file.txt" should output: "/user/file.txt"
