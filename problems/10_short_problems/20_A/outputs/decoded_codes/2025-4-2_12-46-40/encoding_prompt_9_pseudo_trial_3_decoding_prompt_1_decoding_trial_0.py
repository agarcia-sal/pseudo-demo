# Step 1: Receive Input
filePath = input().strip()  # Read input and remove whitespace

# Step 2: Normalize the File Path
# We can use `os.path.normpath` for normalization, which is part of the standard library
import os
normalizedPath = os.path.normpath(filePath)

# Step 3: Adjust the Path
finalPath = normalizedPath

# Replace multiple leading slashes with a single root slash
if finalPath.startswith('//'):
    finalPath = '/' + finalPath.lstrip('/')

# Step 4: Output the Result
print(finalPath)
