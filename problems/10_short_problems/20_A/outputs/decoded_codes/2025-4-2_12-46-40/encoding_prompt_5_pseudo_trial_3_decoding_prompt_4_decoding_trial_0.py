import re
import sys

def normalize_file_path():
    # Step 1.1: Read input file path from standard input
    file_path = input().strip()
    
    # Step 1.2: Normalize the path by removing redundant slashes using regex
    normalized_path = re.sub(r'(?<!:)/+', '/', file_path)  # Replace multiple slashes with a single slash

    # Step 1.3: Ensure the path starts with exactly one forward slash
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path

    # Step 1.4: Output the modified path
    print(normalized_path)

# Execute the normalization process
normalize_file_path()
