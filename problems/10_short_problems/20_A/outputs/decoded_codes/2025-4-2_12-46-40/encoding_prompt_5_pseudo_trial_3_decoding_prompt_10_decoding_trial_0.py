import re
import sys
import posixpath

def normalize_file_path():
    # Step 1.1: Read a string input representing the file path
    file_path = sys.stdin.read().strip()
    
    # Step 1.2: Normalize the path to remove redundant slashes
    normalized_path = posixpath.normpath(file_path)
    
    # Step 1.3: Ensure the path starts with exactly one forward slash
    # Use regex to replace leading slashes with a single slash
    normalized_path = re.sub(r'^/+', '/', normalized_path)

    # Step 1.4: Output the finalized normalized file path
    print(normalized_path)

# Calling the function to execute the normalization process
normalize_file_path()
