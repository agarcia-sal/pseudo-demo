import os

# Step 1: Read Input
input_path = input().strip()

# Step 2: Normalize Path
normalized_path = os.path.normpath(input_path)

# Step 3: Modify Leading Slashes
if normalized_path.startswith('/'):
    # Replace leading slashes with a single forward slash
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 4: Output Result
print(normalized_path)
