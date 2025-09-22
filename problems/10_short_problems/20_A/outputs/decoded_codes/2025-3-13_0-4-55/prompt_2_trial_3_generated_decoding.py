# Start Program

# Read a sequence of characters from standard input which represents a file path
file_path = input().strip()  # Remove leading and trailing spaces

# Normalize the file path
normalized_path = []

# Split the path by slashes, filter out any empty segments, and join back with a single slash
for segment in file_path.split('/'):
    if segment:  # Only include non-empty segments
        normalized_path.append(segment)

# Join the normalized segments back into a single path with slashes
normalized_path = '/'.join(normalized_path)

# If normalized path starts with one or more slashes, replace them with a single slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Display the modified file path
print(normalized_path)

# End Program
