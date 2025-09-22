import os

# Get the file path input from the user
path_string = input()

# Step 1: Trim whitespace from the path
trimmed_path = path_string.strip()

# Step 2: Normalize the path
normalized_path = os.path.normpath(trimmed_path)

# Step 3: Replace multiple leading slashes with a single slash
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/').replace('//', '/')
else:
    cleaned_path = normalized_path

# Step 4: Output the final cleaned path
print(cleaned_path)
