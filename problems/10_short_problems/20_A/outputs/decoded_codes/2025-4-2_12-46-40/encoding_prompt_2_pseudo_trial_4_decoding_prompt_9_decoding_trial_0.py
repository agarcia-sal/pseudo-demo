import os

# Step 1: Read Input
inputPath = input().strip()  # Get the entire input and remove any leading or trailing whitespace

# Step 2: Normalize Path
normalizedPath = os.path.normpath(inputPath)  # Normalize the path using os module

# Step 3: Remove Leading Slashes
# Replace leading slashes with a single slash
if normalizedPath.startswith('/'):
    modifiedPath = '/' + normalizedPath.lstrip('/')
else:
    modifiedPath = normalizedPath

# Step 4: Output Result
print(modifiedPath)  # Display the modified path
