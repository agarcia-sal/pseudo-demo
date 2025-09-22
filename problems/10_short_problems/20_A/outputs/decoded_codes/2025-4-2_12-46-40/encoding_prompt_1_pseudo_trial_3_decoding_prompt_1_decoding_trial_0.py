# Step 1: Read a string input representing a file path from standard input
pathString = input()

# Step 2: Remove any leading or trailing whitespace from the input path
trimmedPath = pathString.strip()

# Step 3: Normalize the path using os.path methods
import os

normalizedPath = os.path.normpath(trimmedPath)

# Step 4: Replace any instances of multiple consecutive leading slashes with a single leading slash
# The following code handles the leading slashes
if normalizedPath.startswith('/'):
    # Split the path on the leading slashes and rejoin it
    cleanedPath = '/' + normalizedPath.lstrip('/').replace('//', '/')
else:
    cleanedPath = normalizedPath.replace('//', '/')

# Step 5: Print the cleaned and normalized file path to standard output
print(cleanedPath)
