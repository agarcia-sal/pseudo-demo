import os

# Step 1: Read Input
input_path = input()

# Step 2: Normalize the File Path
# Normalize the path using os.path.normpath
normalized_path = os.path.normpath(input_path)

# Step 3: Remove Leading Slashes
# Remove leading slashes by replacing them with a single slash
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')
else:
    cleaned_path = normalized_path

# Step 4: Output the Final Path
print(cleaned_path)
