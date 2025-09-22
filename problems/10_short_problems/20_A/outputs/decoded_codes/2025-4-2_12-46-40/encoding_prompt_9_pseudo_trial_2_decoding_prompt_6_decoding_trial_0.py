# Step 1: Import necessary libraries
import os

# Step 2: Get Input
file_path = input().strip()  # Read the file path from user input and remove surrounding whitespace

# Step 3: Normalize the Path
normalized_path = os.path.normpath(file_path)  # Normalize the path using os.path.normpath

# Step 4: Ensure Proper Format
if normalized_path.startswith('/'):
    # Replace multiple leading slashes with a single slash
    normalized_path = '/' + normalized_path.lstrip('/')
else:
    # If it doesn't start with a forward slash, prepend one
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 5: Display Result
print(normalized_path)  # Output the final normalized file path
