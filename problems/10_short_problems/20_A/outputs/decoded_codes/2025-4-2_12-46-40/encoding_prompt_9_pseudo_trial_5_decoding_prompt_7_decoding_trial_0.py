import os

# Step 1: Read Input
# Obtain a string input representing a file path from the user
file_path = input()

# Step 2: Normalize the File Path
# Use the os.path.normpath to normalize the path by resolving redundant separators
normalized_path = os.path.normpath(file_path)

# Step 3: Remove Leading Slashes
# Check if the normalized path has leading slashes and replace them
# Using lstrip to remove all leading slashes and adding a single slash at the start only if the path is not empty
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')
else:
    cleaned_path = normalized_path

# Step 4: Output the Final Path
# Print the cleaned file path
print(cleaned_path)
