# Receive Input
filePath = input().strip()  # Read input and remove whitespace

# Normalize the File Path
normalizedPath = filePath.replace('//', '/')  # Replace double slashes with single (basic normalization)
normalizedPath = normalizedPath.replace('/./', '/')  # Remove current directory references
while '/../' in normalizedPath:  # Resolve parent directory references
    normalizedPath = normalizedPath.replace('/../', '/')

# Adjust the Path
finalPath = normalizedPath
if finalPath.startswith('//'):  # Check for multiple leading slashes
    finalPath = '/' + finalPath.lstrip('/')  # Replace with a single leading slash

# Output the Result
print(finalPath)
