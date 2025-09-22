# Begin Program

# Input Handling: Read a string of text from standard input
inputPath = input().strip()  # Remove leading/trailing whitespace

# Normalize File Path: Replace backslashes with slashes and resolve redundant slashes
normalizedPath = inputPath.replace('\\', '/')

# Adjust Leading Slashes: Ensure that leading slashes are reduced to a single slash
if normalizedPath.startswith('/'):
    finalPath = '/' + normalizedPath.lstrip('/')
else:
    finalPath = normalizedPath.lstrip('/')

# Output Result: Display the final path
print(finalPath)

# End Program
