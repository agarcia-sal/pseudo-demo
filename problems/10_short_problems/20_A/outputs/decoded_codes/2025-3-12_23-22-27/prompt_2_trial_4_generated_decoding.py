# Start Program

# Read a sequence of characters as file path input
file_path = input().strip()  # Remove leading and trailing spaces

# Normalize the file path by eliminating redundant slashes
normalized_path = '/'.join(part for part in file_path.split('/') if part)

# If the normalized path starts with one or more slashes, replace them with a single slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Display the modified file path
print(normalized_path)

# End Program
