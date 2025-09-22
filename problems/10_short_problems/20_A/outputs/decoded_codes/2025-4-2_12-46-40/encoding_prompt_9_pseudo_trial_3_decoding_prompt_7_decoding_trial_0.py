# Receive Input
filePath = input().strip()  # Read input and remove any leading or trailing whitespace

# Normalize the File Path
# Split the path into components based on '/'
path_components = filePath.split('/')
normalized_components = []

# Process each component
for component in path_components:
    # Skip empty components or unnecessary '.' references
    if component == '' or component == '.':
        continue
    # Handle '..' references by popping the last valid component if it exists
    elif component == '..':
        if normalized_components:  # Ensure there is a component to remove
            normalized_components.pop()
    else:
        normalized_components.append(component)  # Add valid path components

# Adjust the Path to ensure it starts with a single root slash
normalizedPath = '/' + '/'.join(normalized_components)  # Join components with a single '/'
finalPath = normalizedPath

# Output the Result
print(finalPath)  # Print the normalized path
