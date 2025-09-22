import os

# Step 1: Read Input
input_path = input().strip()  # Capture and trim whitespace from the standard input

# Step 2: Normalize File Path
# Using os.path.normpath to normalize the file path
normalized_path = os.path.normpath(input_path)

# Ensure the resulting path starts with a single forward slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 3: Output Result
print(normalized_path)  # Print the normalized file path
