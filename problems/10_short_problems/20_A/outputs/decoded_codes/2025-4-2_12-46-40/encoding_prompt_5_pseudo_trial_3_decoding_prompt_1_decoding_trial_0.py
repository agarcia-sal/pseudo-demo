import re
import posixpath

def NormalizeFilePath():
    # Step 1.1: Read a string from standard input which represents the file path
    file_path = input()
    
    # Step 1.2: Normalize the path using posixpath.normpath to eliminate redundant parts
    normalized_path = posixpath.normpath(file_path)
    
    # Step 1.3: Ensure the output starts with exactly one forward slash
    if normalized_path.startswith('/'):
        # Replace all leading slashes with exactly one
        normalized_path = re.sub(r'^/+','/', normalized_path)
    else:
        # Ensure it starts with one slash if it does not
        normalized_path = '/' + normalized_path
    
    # Step 1.4: Print the finalized normalized file path
    print(normalized_path)

# Step 2: Call the NormalizeFilePath function to execute the normalization process
NormalizeFilePath()
