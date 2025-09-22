def normalize_file_path():
    # Step 2: Read Input
    file_path = input().strip()  # Obtain a string input and remove leading/trailing spaces
    
    # Step 3: Normalize the File Path
    # Replace any sequence of slashes at the beginning of the path with a single slash
    while file_path.startswith('/'):
        file_path = file_path[1:]  # Remove the leading slash
    normalized_path = '/' + file_path  # Add a single leading slash back
    
    # Step 4: Output the Result
    print(normalized_path)  # Display the modified file path

# Call the function to execute the normalization process
normalize_file_path()
