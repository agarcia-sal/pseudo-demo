# Import necessary modules for path and regex handling
import posixpath
import sys
import re

def normalize_file_path():
    # Read the entire input from the standard input
    raw_path = input()
    
    # Trim leading and trailing whitespace
    trimmed_path = raw_path.strip()
    
    # Normalize the path using posixpath
    normalized_path = posixpath.normpath(trimmed_path)
    
    # Replace multiple leading slashes with a single slash in normalized_path
    cleaned_path = re.sub(r'^\/+', '/', normalized_path)
    
    # Output the final cleaned path
    print(cleaned_path)

# Call the function to normalize the file path
normalize_file_path()
