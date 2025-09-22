import os
import re

def normalize_and_clean_file_path():
    # Step 1: Read input from the user, stripping leading and trailing whitespace.
    input_string = input().strip()
    
    # Step 2: Normalize the path using os.path.normpath which handles the path formatting.
    normalized_path = os.path.normpath(input_string)
    
    # Step 3: Clean up the path to ensure leading slashes are formatted correctly.
    # This regex replaces multiple leading slashes with a single one if found.
    cleaned_path = re.sub(r'^/+', '/', normalized_path)
    
    # Step 4: Output the cleaned path.
    print(cleaned_path)

# If you want to run the function, uncomment the line below:
# normalize_and_clean_file_path()
