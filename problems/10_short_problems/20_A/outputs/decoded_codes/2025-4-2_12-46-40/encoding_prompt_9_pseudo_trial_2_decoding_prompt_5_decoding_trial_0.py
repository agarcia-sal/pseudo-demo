import os  # Necessary for path normalization
import re  # Necessary for regular expression handling

def normalize_file_path():
    # Step 1: Get Input
    raw_path = input().strip()  # Read input and remove surrounding whitespace

    # Step 2: Normalize the Path
    normalized_path = os.path.normpath(raw_path)  # Normalize path to eliminate redundant segments

    # Step 3: Ensure Proper Format
    # Replace multiple leading slashes with a single slash
    normalized_path = re.sub(r'^/{2,}', '/', normalized_path)

    # Ensure the path starts with a single forward slash
    if not normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path

    # Step 4: Display Result
    print(normalized_path)  # Output the final processed file path

# Example usage:
# normalize_file_path()  # Uncomment this line to run the function when needed
