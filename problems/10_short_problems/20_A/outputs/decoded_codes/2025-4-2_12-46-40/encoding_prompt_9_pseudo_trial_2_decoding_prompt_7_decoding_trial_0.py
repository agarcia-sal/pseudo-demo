import os  # Import os for path normalization

def normalize_file_path():
    # Step 1: Get Input
    raw_path = input().strip()  # Read the file path and remove surrounding whitespace

    # Step 2: Normalize the Path
    # Use os.path.normpath to collapse redundant separators and up-level references
    normalized_path = os.path.normpath(raw_path)

    # Step 3: Ensure Proper Format
    # Ensure the path starts with a single forward slash
    if normalized_path.startswith('/'):
        # If it starts with multiple slashes, replace them with a single slash
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path  # Prepend a single forward slash

    # Step 4: Display Result
    print(normalized_path)  # Output the normalized file path

# Execute the function
normalize_file_path()
