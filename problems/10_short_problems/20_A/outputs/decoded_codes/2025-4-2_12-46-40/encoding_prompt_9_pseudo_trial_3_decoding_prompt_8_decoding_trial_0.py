import os

# Step 1: Receive Input
filePath = input().strip()

# Step 2: Normalize the File Path
normalizedPath = os.path.normpath(filePath)

# Step 3: Adjust the Path
if normalizedPath.startswith('//'):
    finalPath = '/' + normalizedPath.lstrip('/')
else:
    finalPath = normalizedPath

# Step 4: Output the Result
print(finalPath)
