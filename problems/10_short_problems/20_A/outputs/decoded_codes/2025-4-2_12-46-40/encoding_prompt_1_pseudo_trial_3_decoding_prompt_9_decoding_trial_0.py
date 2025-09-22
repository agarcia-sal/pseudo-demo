import os

# Read input for the file path
path_string = input()

# Step 1: Trim whitespace from the path
trimmed_path = path_string.strip()

# Step 2: Normalize the path using the file system conventions
normalized_path = os.path.normpath(trimmed_path)

# Step 3: Replace multiple leading slashes with a single slash
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')
else:
    cleaned_path = normalized_path.lstrip('/')

# Step 4: Output the final cleaned path
print(cleaned_path)
