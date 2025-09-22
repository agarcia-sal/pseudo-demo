import re
import posixpath

def NormalizeFilePath():
    # Read the input file path from the user
    file_path = input().strip()
    
    # Normalize the path by removing redundant separators
    normalized_path = posixpath.normpath(file_path)
    
    # Ensure the path starts with exactly one forward slash
    # Replace any leading slashes with a single slash
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path

    # Output the modified path to the user
    print(normalized_path)

# Call the NormalizeFilePath function to execute the normalization process
NormalizeFilePath()
