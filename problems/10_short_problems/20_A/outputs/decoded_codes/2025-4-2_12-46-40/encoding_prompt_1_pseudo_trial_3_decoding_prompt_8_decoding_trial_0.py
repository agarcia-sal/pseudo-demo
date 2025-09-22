import os

# Step 1: Read the input path from standard input
pathString = input()

# Step 2: Trim whitespace from the path
trimmedPath = pathString.strip()

# Step 3: Normalize the path
normalizedPath = os.path.normpath(trimmedPath)

# Step 4: Replace multiple leading slashes with a single slash
if normalizedPath.startswith('/'):
    cleanedPath = '/' + normalizedPath.lstrip('/')
else:
    cleanedPath = normalizedPath.lstrip('/')

# Step 5: Output the final cleaned path
print(cleanedPath)
