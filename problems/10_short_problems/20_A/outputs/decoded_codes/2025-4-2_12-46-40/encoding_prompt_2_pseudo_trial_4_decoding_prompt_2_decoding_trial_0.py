import os  # To normalize the path

# 1. Read Input
inputPath = input().strip()

# 2. Normalize Path
normalizedPath = os.path.normpath(inputPath)

# 3. Remove Leading Slashes
if normalizedPath.startswith('/'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# 4. Output Result
print(normalizedPath)
