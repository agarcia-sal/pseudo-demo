# Start Program

# Read a sequence of characters from standard input
file_path = input().strip()  # Remove leading and trailing spaces

# Normalize the path by replacing multiple consecutive slashes with a single slash
normalized_path = '/'.join(part for part in file_path.split('/') if part)

# If the normalized path begins with one or more slashes, adjust to a single leading slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Display the modified file path
print(normalized_path)

# End Program
