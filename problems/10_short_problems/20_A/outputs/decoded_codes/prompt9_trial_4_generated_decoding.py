import os

# Step 1: Receive Input
# Get the file path from user input
inputPath = input()

# Step 2: Normalize the Path
# Normalize the path using os.path.normpath to standardize the format
normalizedPath = os.path.normpath(inputPath)

# Step 3: Remove Leading Slashes
# If normalizedPath starts with one or more slashes, replace with a single leading slash
if normalizedPath.startswith('/'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# Step 4: Display Output
# Print the cleaned-up file path
print(normalizedPath)
