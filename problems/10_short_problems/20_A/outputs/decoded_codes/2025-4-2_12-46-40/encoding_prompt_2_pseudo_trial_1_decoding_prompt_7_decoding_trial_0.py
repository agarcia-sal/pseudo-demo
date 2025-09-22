# Function to normalize a file path
def normalize_file_path():
    # Step 2: Read Input
    # Obtain a string input from user and remove leading/trailing spaces
    file_path = input().strip()
    
    # Step 3: Normalize the File Path
    # If the path starts with one or more slashes, replace with a single slash
    if file_path.startswith('/'):
        # Normalize by replacing any leading slashes with a single slash
        normalized_path = '/' + file_path.lstrip('/')
    else:
        # If there are no leading slashes, just return the cleaned path
        normalized_path = file_path
    
    # Step 4: Output the Result
    print(normalized_path)

# Call the function to execute the normalization
normalize_file_path()
