import os

# Read input path from standard input
inputPath = input()

# Normalize the input path
normalizedPath = os.path.normpath(inputPath)

# Remove leading slashes, ensuring at least one leading slash remains
if normalizedPath.startswith('/'):
    resultPath = '/' + normalizedPath.lstrip('/')
else:
    resultPath = '/' + normalizedPath

# Output the final processed path
print(resultPath)
