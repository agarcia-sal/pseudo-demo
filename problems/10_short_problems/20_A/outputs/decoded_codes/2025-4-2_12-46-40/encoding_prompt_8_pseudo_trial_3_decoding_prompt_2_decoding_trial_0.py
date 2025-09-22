import os

# Step 1: Read input
originalPath = input()
trimmedPath = originalPath.strip()

# Step 2: Normalize the file path
normalizedPath = os.path.normpath(trimmedPath)

# Step 3: Ensure the path starts with a single forward slash
if normalizedPath.startswith('/'):
    finalPath = '/' + normalizedPath.lstrip('/')
else:
    finalPath = '/' + normalizedPath 

# Step 4: Output the final result
print(finalPath)
