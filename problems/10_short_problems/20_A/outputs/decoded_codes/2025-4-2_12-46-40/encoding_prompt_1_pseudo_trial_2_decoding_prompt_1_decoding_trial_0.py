# Start Program

# Get Input
inputString = input().strip()

# Normalize Path
import os
normalizedPath = os.path.normpath(inputString)

# Clean Path
if normalizedPath.startswith('/'):
    cleanedPath = '/' + normalizedPath.lstrip('/')
else:
    cleanedPath = normalizedPath.lstrip('/')

# Output Result
print(cleanedPath)

# End Program
