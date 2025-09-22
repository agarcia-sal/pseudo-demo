def normalize_file_path():
    # Step 2: Read input, removing any leading and trailing spaces
    file_path = input().strip()
    
    # Step 3: Normalize the file path
    # Replace leading slashes with a single leading slash,
    # followed by the remaining path (if any)
    normalized_path = '/' + file_path.lstrip('/')

    # Step 4: Output the result
    print(normalized_path)

# Uncomment the line below to run the function directly
# normalize_file_path()
