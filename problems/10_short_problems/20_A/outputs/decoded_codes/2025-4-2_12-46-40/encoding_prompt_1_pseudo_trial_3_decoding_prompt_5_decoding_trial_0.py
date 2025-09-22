import os

def clean_and_normalize_path():
    # Step 1: Read a string input representing a file path
    path_string = input().strip()

    # Step 2: Normalize the path
    normalized_path = os.path.normpath(path_string)

    # Step 3: Replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        # Count the number of leading slashes
        leading_slashes = len(normalized_path) - len(normalized_path.lstrip('/'))
        # Create a cleaned path with a single leading slash
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path

    # Step 4: Output the final cleaned path
    print(cleaned_path)

# Example usage (commented out for testing purposes):
# clean_and_normalize_path()  # Input can be given during execution for testing
