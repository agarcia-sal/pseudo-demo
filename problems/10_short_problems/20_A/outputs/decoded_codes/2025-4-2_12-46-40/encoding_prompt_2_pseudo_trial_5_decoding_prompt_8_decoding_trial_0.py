import os

# Read Input
input_path = input().strip()

# Normalize Path
normalized_path = os.path.normpath(input_path)

# Modify Leading Slashes
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Output Result
print(normalized_path)
