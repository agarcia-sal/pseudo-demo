import os

# Read the file path input from standard input and remove leading/trailing whitespace
file_path = input().strip()

# Normalize the file path by resolving redundant elements
normalized_path = os.path.normpath(file_path)

# Ensure the normalized path starts with a single root slash
final_path = '/' + normalized_path.lstrip('/')

# Print the final result
print(final_path)
