import os
import re

def normalize_and_clean_path():
    # STEP 1: Read user input
    raw_path_string = input()
    
    # STEP 2: Normalize the path
    normalized_path = normalize_path(raw_path_string)
    
    # STEP 3: Remove unnecessary leading slashes
    cleaned_path = remove_leading_slashes(normalized_path)
    
    # STEP 4: Print the cleaned path as output
    print(cleaned_path)

def normalize_path(path):
    # Normalize path using os.path.normpath which standardizes path separators
    standardized_path = os.path.normpath(path)
    return standardized_path

def remove_leading_slashes(path):
    # Use regular expression to replace one or more leading slashes with a single slash
    cleaned_path = re.sub(r'^/+', '/', path)
    return cleaned_path

# MAIN EXECUTION
normalize_and_clean_path()
