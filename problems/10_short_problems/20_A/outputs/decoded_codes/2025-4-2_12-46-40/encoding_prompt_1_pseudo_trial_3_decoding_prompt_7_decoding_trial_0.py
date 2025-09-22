import os

def normalize_and_clean_path():
    # Step 1: Read a string input representing a file path from standard input
    path_string = input()  # Get the raw input path from the user

    # Step 1: Trim whitespace from the path
    trimmed_path = path_string.strip()  # Remove leading and trailing whitespace

    # Step 2: Normalize the path
    normalized_path = os.path.normpath(trimmed_path)  # Normalize using file system conventions

    # Step 3: Replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        # If it starts with a '/', replace multiple leading slashes with a single one
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path.lstrip('/')  # Just remove leading slashes if none at start
    
    # Step 4: Output the final cleaned path
    print(cleaned_path)  # Print the cleaned and normalized path

# Run the normalization function
normalize_and_clean_path()
