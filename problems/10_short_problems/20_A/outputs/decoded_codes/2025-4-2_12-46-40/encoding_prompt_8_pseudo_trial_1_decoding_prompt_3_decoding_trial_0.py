import posixpath
import sys
import re

def normalize_path():
    # Step 2: Read input path
    input_path = input().strip()

    # Step 3: Normalize the path using posixpath
    normalized_path = posixpath.normpath(input_path)

    # Step 4: Ensure leading forward slash
    # Replace any leading slashes in the normalized path with a single '/'
    final_path = re.sub(r'^/+','/', normalized_path)

    # Step 5: Output the final path
    print(final_path)

# Call the function to execute the normalization
normalize_path()
