def normalize_file_path():
    # Step 1: Read input for the file path
    file_path = input().strip()  # Remove leading and trailing spaces
    
    # Step 2: Normalize the file path
    # Replace leading sequences of slashes with a single slash
    while file_path.startswith('/'):
        file_path = file_path[1:]  # Remove the leading slash
    normalized_path = '/' + file_path  # Add a single leading slash

    # Step 3: Output the normalized file path
    print(normalized_path)

# Example of testing with different inputs:
# Input: "///usr/local/bin"
# Output: "/usr/local/bin"
#
# Input: "    /home/user/documents   "
# Output: "/home/user/documents"
