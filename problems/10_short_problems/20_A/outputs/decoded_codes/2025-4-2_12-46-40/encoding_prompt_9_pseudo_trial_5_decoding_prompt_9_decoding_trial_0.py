# Read Input: Obtain a file path from the user
file_path = input()

# Normalize the File Path: Clean the path by resolving redundant separators
normalized_path = file_path.replace('//', '/').replace('./', '').replace('/./', '/')

# Remove Leading Slashes: Ensure there's only one leading slash
while normalized_path.startswith('/'):
    normalized_path = normalized_path[1:]

# If there are any segments left, add a leading slash
if normalized_path:
    normalized_path = '/' + normalized_path

# Output the Final Path: Print the cleaned file path
print(normalized_path)
