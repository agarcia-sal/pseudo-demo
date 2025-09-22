import os

def normalize_file_path():
    # Step 1: Read Input
    file_path = input()  # Read the file path from standard input

    # Step 2: Normalize the File Path
    # Normalize the path using os.path.normpath() to handle any redundant separators and up-level references.
    normalized_path = os.path.normpath(file_path)

    # Step 3: Remove Leading Slashes
    # Strip leading slashes and ensure a single leading slash if the path is not empty
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 4: Output the Final Path
    print(normalized_path)

# Example usage: Uncomment below to run the function
# normalize_file_path()
