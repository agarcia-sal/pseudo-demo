import os

# Step 1: Read a string input representing a file path
path_string = input()

# Step 2: Trim whitespace from the path
trimmed_path = path_string.strip()

# Step 3: Normalize the path
# This uses 'os.path.normpath' to resolve any symbolic links or relative components
normalized_path = os.path.normpath(trimmed_path)

# Step 4: Replace multiple leading slashes with a single slash
# Check if the normalized path starts with multiple slashes and replace them
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')
else:
    cleaned_path = normalized_path

# Step 5: Output the final cleaned path
print(cleaned_path)
