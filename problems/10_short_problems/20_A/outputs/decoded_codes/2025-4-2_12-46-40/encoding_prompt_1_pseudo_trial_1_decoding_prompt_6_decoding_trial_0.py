import os

# Step 2: Read input (file path)
file_path = input()

# Step 3: Remove extra whitespace (trim)
trimmed_path = file_path.strip()

# Step 4: Normalize the file path
normalized_path = os.path.normpath(trimmed_path)

# Step 5: Adjust leading slashes
if normalized_path.startswith('/'):
    adjusted_path = '/' + normalized_path.lstrip('/')
else:
    adjusted_path = normalized_path

# Step 6: Output the result
print(adjusted_path)
