# Read input path from standard input
inputPath = input()

# Normalize the input path (this is a placeholder for normalization logic)
normalizedPath = normalize_path(inputPath)  # You would define normalize_path to handle POSIX normalization

# Remove leading slashes, ensuring at least one leading slash remains
if normalizedPath.startswith('/'):
    resultPath = '/' + normalizedPath.lstrip('/')
else:
    resultPath = '/' + normalizedPath

# Output the final processed path
print(resultPath)
