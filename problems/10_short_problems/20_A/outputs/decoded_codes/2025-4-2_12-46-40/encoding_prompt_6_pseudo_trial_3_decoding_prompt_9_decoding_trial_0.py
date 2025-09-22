import os

# Read input from standard input and remove any leading/trailing whitespace
input_string = input().strip()

# Normalize the path to a standard format
normalized_path = os.path.normpath(input_string)

# Replace sequences of leading slashes with a single slash
if normalized_path.startswith('/'):
    # Replace leading slashes
    updated_path = '/' + normalized_path.lstrip('/')
else:
    updated_path = normalized_path

# Output the final transformed path
print(updated_path)
