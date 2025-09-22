import os
import re

def normalize_and_clean_file_path():
    # Read input from the user
    input_string = input().strip()  # Remove leading and trailing whitespace

    # Normalize the path
    normalized_path = os.path.normpath(input_string)  # Normalize the input string to a standard path format

    # Clean up leading slashes
    cleaned_path = re.sub(r'^/+','/', normalized_path)  # Replace multiple leading slashes with a single slash

    # Output the result
    print(cleaned_path)

# Example test case (commented out for actual use)
# Input: "//folder//subfolder//file.txt"
# Output: "/folder/subfolder/file.txt"
