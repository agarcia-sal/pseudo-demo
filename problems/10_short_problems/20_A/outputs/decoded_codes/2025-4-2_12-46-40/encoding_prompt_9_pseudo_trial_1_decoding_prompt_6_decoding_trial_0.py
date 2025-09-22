import os  # Importing os module to help normalize the path

# Step 1: Receive Input
path_input = input().strip()  # Read input and remove extra spaces

# Step 2: Normalize Path
normalized_path = os.path.normpath(path_input)  # Normalize the path using os.path.normpath

# Step 3: Ensure Single Leading Slash
if normalized_path.startswith('//'):  # Check if path starts with multiple slashes
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace with a single leading slash

# Step 4: Output Result
print(normalized_path)  # Print the final normalized path
