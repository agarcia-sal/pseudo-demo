import os

# Read input from standard input and strip whitespace
input_path = input().strip()

# Normalize the path
normalized_path = os.path.normpath(input_path)

# Modify leading slashes
if normalized_path.startswith('/'):
    # Replace leading slashes with a single forward slash
    normalized_path = '/' + normalized_path.lstrip('/')

# Output the result
print(normalized_path)
