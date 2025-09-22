import os

# Read input path from standard input
input_path = input()

# Normalize the input path using POSIX standards
normalized_path = os.path.normpath(input_path)

# Remove leading slashes, ensuring at least one leading slash remains
if normalized_path.startswith('/'):
    result_path = '/' + normalized_path.lstrip('/')
else:
    result_path = '/' + normalized_path

# Output the final processed path
print(result_path)
