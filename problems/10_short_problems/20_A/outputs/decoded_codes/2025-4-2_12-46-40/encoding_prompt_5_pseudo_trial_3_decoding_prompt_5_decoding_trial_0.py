import re
import posixpath

def NormalizeFilePath():
    # Step 1.1: Read a string input which represents the file path
    file_path = input()
    
    # Step 1.2: Normalize the path to remove redundant slashes
    normalized_path = posixpath.normpath(file_path)  # Normalize the path by removing redundant slashes
    
    # Step 1.3: Ensure the output starts with exactly one forward slash
    if normalized_path.startswith("/"):
        # Replace multiple leading slashes with a single slash
        normalized_path = re.sub(r'^/+', '/', normalized_path)
    else:
        # If it doesn't start with a slash, just add one
        normalized_path = '/' + normalized_path
    
    # Step 1.4: Output the finalized normalized file path
    print(normalized_path)

# Call the NormalizeFilePath function to execute the normalization process
NormalizeFilePath()
