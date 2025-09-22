import sys
import posixpath
import re

def NormalizeFilePath():
    # 1.1. Read a string from standard input which represents the file path.
    file_path = sys.stdin.read().strip()

    # 1.2. Normalize the path using posixpath.normpath to eliminate redundant parts.
    normalized_path = posixpath.normpath(file_path)

    # 1.3. Ensure the output starts with a single forward slash.
    # Replace all leading slashes with exactly one slash.
    modified_path = re.sub(r'^/+', '/', normalized_path)

    # 1.4. Output the finalized normalized file path.
    print(modified_path)

# 2. Call the NormalizeFilePath function to execute the normalization process.
NormalizeFilePath()
