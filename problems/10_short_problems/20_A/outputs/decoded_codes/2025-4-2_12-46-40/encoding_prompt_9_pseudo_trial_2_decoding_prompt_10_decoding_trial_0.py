import os
import re

def normalize_file_path():
    # Step 1: Get Input
    raw_path = input().strip()

    # Step 2: Normalize the Path
    # Use os.path.normpath to standardize the path format.
    normalized_path = os.path.normpath(raw_path)

    # Step 3: Ensure Proper Format
    # Replace multiple leading forward slashes with a single one.
    # Note: we will check if the path starts with a forward slash to ensure it's properly formatted.
    if normalized_path.startswith('/'):
        final_path = re.sub(r'^/+','/', normalized_path)
    else:
        final_path = '/' + normalized_path

    # Step 4: Display Result
    print(final_path)

# Call the function to execute the path normalization
normalize_file_path()
