import os

# Step 1: Read Input
inputPath = input().strip()

# Step 2: Normalize File Path
normalizedPath = os.path.normpath('/' + inputPath.replace('\\', '/')).replace('//', '/')

# Ensure that the normalized path starts with a single slash
if normalizedPath.startswith('//'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# Step 3: Output Result
print(normalizedPath)
