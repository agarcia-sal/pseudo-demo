import os
import re

def normalize_file_path():
    # Step 1: Read the file path from standard input and remove extra spaces
    file_path = input().strip()

    # Step 2: Normalize the file path using system path conventions
    normalized_path = os.path.normpath(file_path)

    # Step 3: Remove leading slashes (replace with a single slash)
    final_path = re.sub(r'^/+','/', normalized_path)

    # Step 4: Output the result
    print(final_path)

# Uncomment the following line to execute the function
# normalize_file_path()
