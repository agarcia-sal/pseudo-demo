import os

def normalize_file_path():
    # Step 2: Read Input
    file_path = input().strip()  # Read a string and trim whitespace

    # Step 4: Normalize the File Path
    normalized_path = os.path.normpath(file_path)

    # Step 5: Adjust Leading Slashes
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 6: Output the Result
    print(normalized_path)

# Run the function
normalize_file_path()
