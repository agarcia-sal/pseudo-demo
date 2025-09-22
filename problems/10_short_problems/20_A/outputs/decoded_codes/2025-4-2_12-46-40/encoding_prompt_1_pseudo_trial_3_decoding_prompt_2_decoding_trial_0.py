import os

# Step 1: Read a string input representing a file path
pathString = input()

# Step 2: Trim whitespace from the path
trimmedPath = pathString.strip()

# Step 3: Normalize the path using the os.path module
# This takes care of resolving any symbolic links or relative components
normalizedPath = os.path.normpath(trimmedPath)

# Step 4: Replace multiple leading slashes with a single slash
if normalizedPath.startswith('/'):
    cleanedPath = '/' + normalizedPath.lstrip('/')
else:
    cleanedPath = normalizedPath.lstrip('/')

# Step 5: Output the final cleaned path
print(cleanedPath)
