# Start Program

# Read a sequence of characters from standard input (file path)
file_path = input().strip()  # Remove leading and trailing spaces

# Normalize the file path by replacing multiple slashes with a single slash
normalized_path = []
previous_char = ''

for char in file_path:
    if char == '/' and previous_char == '/':
        continue  # Skip this character as it's a redundant slash
    normalized_path.append(char)
    previous_char = char

normalized_path = ''.join(normalized_path)  # Join the list back into a string

# If the normalized path starts with one or more slashes, replace with a single slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Display the modified file path
print(normalized_path)

# End Program
