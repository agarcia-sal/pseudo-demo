# Start Program

# Read a sequence of characters from standard input, representing a file path
file_path = input().strip()

# Normalize the file path by removing redundant slashes
normalized_path = '/'.join(part for part in file_path.split('/') if part)

# If the normalized path starts with multiple slashes, replace them with a single slash
if normalized_path.startswith('/'):
    modified_path = '/' + normalized_path.lstrip('/')
else:
    modified_path = normalized_path

# Display the modified file path
print(modified_path)

# End Program
