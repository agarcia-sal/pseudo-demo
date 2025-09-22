import os
import re

def normalize_and_clean_file_path():
    # Step 1: Read input from the user and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Step 2: Normalize the path using os.path.normpath
    normalized_path = os.path.normpath(input_string)
    
    # Step 3: Clean up the path to replace multiple leading slashes with a single slash
    cleaned_path = re.sub(r'^/+','/', normalized_path)
    
    # Step 4: Print the cleaned path
    print(cleaned_path)

# To execute the function
if __name__ == "__main__":
    normalize_and_clean_file_path()
