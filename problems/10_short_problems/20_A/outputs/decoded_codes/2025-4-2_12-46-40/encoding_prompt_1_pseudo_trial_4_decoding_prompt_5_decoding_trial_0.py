def normalize_file_path():
    # Read the input path from the user and trim leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the path by replacing multiple slashes with a single slash
    # and using a list to eliminate redundant components
    parts = input_path.split('/')
    
    # Use list comprehension to filter out empty parts resulting from redundant slashes
    normalized_parts = [part for part in parts if part]
    
    # Join the parts back together with a single slash
    normalized_path = '/' + '/'.join(normalized_parts)
    
    # Print the normalized file path
    print(normalized_path)

# Example test cases:
# If input is "///usr//local/bin///", the output will be "/usr/local/bin"
# If input is "//home//user/", the output will be "/home/user"
