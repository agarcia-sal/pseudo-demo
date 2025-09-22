# Start

# Read Input:
inputPath = input().strip()

# Normalize Path:
import os
normalizedPath = os.path.normpath(inputPath)

# Reduce Leading Slashes:
finalPath = normalizedPath.lstrip('/')
if finalPath.startswith('/'):
    finalPath = '/' + finalPath.lstrip('/')

# Output Result:
print(finalPath)

# End
