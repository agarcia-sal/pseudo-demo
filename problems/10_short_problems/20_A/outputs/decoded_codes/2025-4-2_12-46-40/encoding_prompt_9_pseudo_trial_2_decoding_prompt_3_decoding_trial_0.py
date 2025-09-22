import os
import re

def normalize_file_path():
    # Step 2: Get Input
    file_path = input().strip()  # Read the input path and remove surrounding whitespace

    # Step 3: Normalize the Path
    # Use os.path.normpath to handle the normalization of paths
    normalized_path = os.path.normpath(file_path)
    
    # Step 4: Ensure Proper Format
    # Replace any leading slashes with a single '/'
    normalized_path = re.sub(r'^/+','/', normalized_path)

    # Check if the path is not empty after normalization
    if normalized_path == '':
        normalized_path = '/'

    # Step 5: Display Result
    print(normalized_path)

# The function can be called to perform the normalization.
normalize_file_path()
