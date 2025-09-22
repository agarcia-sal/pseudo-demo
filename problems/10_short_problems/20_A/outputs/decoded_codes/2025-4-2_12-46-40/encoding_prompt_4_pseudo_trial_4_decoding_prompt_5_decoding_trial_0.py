import os

# Read a file path input from standard input
input_path = input()

# Normalize the file path by removing redundant separators
normalized_path = os.path.normpath(input_path)

# Replace any leading slashes with a single leading slash
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')
else:
    cleaned_path = normalized_path.lstrip('/')

# Output the cleaned path
print(cleaned_path)
