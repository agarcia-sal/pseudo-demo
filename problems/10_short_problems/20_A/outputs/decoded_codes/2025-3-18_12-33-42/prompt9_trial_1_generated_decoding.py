import os

# Step 1: Read Input
inputPath = input()

# Step 2: Normalize the File Path
# Using os.path.normpath to normalize the file path
normalizedPath = os.path.normpath(inputPath)

# Step 3: Remove Leading Slashes
# Create cleanedPath by replacing leading slashes with a single one if any exist
cleanedPath = normalizedPath.lstrip('/')
if normalizedPath.startswith('/'):
    cleanedPath = '/' + cleanedPath

# Step 4: Output the Result
print(cleanedPath)
