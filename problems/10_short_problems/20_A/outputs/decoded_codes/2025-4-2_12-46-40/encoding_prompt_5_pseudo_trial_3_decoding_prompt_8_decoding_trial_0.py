import sys
import posixpath
import re

def NormalizeFilePath():
    # Step 1.1: Read a string from standard input which represents the file path.
    file_path = input().strip()

    # Step 1.2: Normalize the path using posixpath.normpath()
    normalized_path = posixpath.normpath(file_path)

    # Step 1.3: Ensure the output starts with a single forward slash
    # Replace multiple leading slashes with a single slash
    modified_path = re.sub(r'^/+', '/', normalized_path)

    # Step 1.4: Output the finalized normalized file path
    print(modified_path)

# Call the function to execute the normalization process
NormalizeFilePath()
