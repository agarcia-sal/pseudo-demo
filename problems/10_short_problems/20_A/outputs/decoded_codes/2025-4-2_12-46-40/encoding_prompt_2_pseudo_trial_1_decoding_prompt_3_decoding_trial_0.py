def normalize_file_path():
    # Step 1: Read input
    file_path = input().strip()  # Remove leading and trailing spaces
    
    # Step 2: Normalize the file path
    # Replace any sequence of leading slashes with a single slash
    while file_path.startswith('/'):
        file_path = file_path[1:]  # Remove the leading slash
    normalized_path = '/' + file_path  # Add a single leading slash back
    
    # Step 3: Output the result
    print(normalized_path)

# Potential test case scenarios can be added here to validate the function
# For example:
# Input: "///usr//bin///python"
# Output should be: "/usr/bin/python"

# This function can now be called to normalize a file path.
normalize_file_path()
