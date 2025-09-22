def normalize_file_path():
    # Step 2: Read Input
    file_path = input().strip()

    # Step 3: Normalize the File Path
    # Replace any sequence of leading slashes with a single slash
    normalized_path = file_path.lstrip('/')

    # Output the single leading slash if the normalized path is not empty
    if normalized_path:
        normalized_path = '/' + normalized_path
    
    # Step 4: Output the Result
    print(normalized_path)

# Call the function to run the process
normalize_file_path()
