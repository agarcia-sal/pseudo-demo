import re
import sys
import posixpath

def NormalizeFilePath():
    # Step 1.1: Read the input file path from the user.
    file_path = input().strip()
    
    # Step 1.2: Normalize the path to remove redundant slashes.
    normalized_path = posixpath.normpath(file_path)
    
    # Step 1.3: Ensure the normalized path starts with exactly one forward slash.
    # Replace all leading slashes with one slash.
    modified_path = re.sub(r'^/+', '/', normalized_path)
    
    # Step 1.4: Output the finalized normalized file path.
    print(modified_path)

# Execute the normalization process.
NormalizeFilePath()
