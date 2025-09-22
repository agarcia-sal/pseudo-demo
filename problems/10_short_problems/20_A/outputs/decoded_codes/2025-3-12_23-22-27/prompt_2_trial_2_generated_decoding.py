# Start Program

# Read a sequence of characters from standard input (a file path)
file_path = input()

# Remove any leading or trailing spaces from the input
file_path = file_path.strip()

# Normalize the file path to eliminate redundant slashes
# We will use a combination of string replacement and splitting/joining
normalized_path = '/'.join(part for part in file_path.split('/') if part)  # Split by '/', filter empty parts, and join with '/'

# If the normalized path begins with one or more slashes, replace with a single slash
if normalized_path.startswith('/'):
    # Replace multiple leading slashes with a single slash
    normalized_path = '/' + normalized_path.lstrip('/')

# Display the modified file path
print(normalized_path)

# End Program
