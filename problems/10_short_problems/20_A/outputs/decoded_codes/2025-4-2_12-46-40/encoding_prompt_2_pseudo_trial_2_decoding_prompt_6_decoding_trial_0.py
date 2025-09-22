import os

# Step 2: Read a line of input from the user
input_file_path = input()

# Step 3: Process Input
# Remove leading or trailing whitespace
normalized_path = input_file_path.strip()
# Normalize the file path
normalized_path = os.path.normpath(normalized_path)

# Step 4: Adjust Path Format
# If the normalized path starts with one or more forward slashes, replace with a single slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 5: Output Result
print(normalized_path)
