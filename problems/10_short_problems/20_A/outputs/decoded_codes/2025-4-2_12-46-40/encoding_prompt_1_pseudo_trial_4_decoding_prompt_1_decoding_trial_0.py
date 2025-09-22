# Step 1: Read Input
inputPath = input().strip()

# Step 2: Normalize File Path
# Normalize the path by replacing redundant slashes and ensuring it starts correctly
normalizedPath = '/'.join(segment for segment in inputPath.split('/') if segment)

# Ensure the path starts with a single forward slash
if normalizedPath.startswith('/'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# Step 3: Output Result
print(normalizedPath)
