# Step 1: Receive Input
filePath = input().strip()  # Read and clean input by removing leading and trailing whitespace

# Step 2: Normalize the File Path
# The normalization process can be achieved by using 'os.path.normpath' for simplicity
import os
normalizedPath = os.path.normpath(filePath)

# Step 3: Adjust the Path
# Checking if the path starts with more than one root slash
if normalizedPath.startswith('//'):
    finalPath = '/' + normalizedPath.lstrip('/')
else:
    finalPath = normalizedPath

# Step 4: Output the Result
print(finalPath)
