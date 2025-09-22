import os
import re

def main():
    # Step 1: Read a path input from the user
    raw_path = input()
    
    # Step 2: Normalize the file path
    normalized_path = normalize_path(raw_path)
    
    # Step 3: Clean up the path by replacing multiple leading slashes with a single slash
    cleaned_path = clean_leading_slashes(normalized_path)
    
    # Step 4: Output the cleaned path
    print(cleaned_path)

def normalize_path(input_path):
    # Use the standard library to normalize the path
    return os.path.normpath(input_path)

def clean_leading_slashes(path):
    # Use a regular expression to substitute one or more leading slashes with a single slash
    return re.sub(r'^[\\/]+', '/', path)

# Run the main function
if __name__ == '__main__':
    main()
