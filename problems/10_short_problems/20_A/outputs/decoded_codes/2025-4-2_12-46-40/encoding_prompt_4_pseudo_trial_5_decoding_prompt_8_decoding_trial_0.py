def normalizePath(path):
    # Normalize file path by replacing backslashes with forward slashes
    return path.replace('\\', '/')

def removeLeadingSlashes(path):
    # Remove leading slashes and replace with a single slash
    return '/' + path.lstrip('/')

# Read input from the standard input (stdin)
input_path = input()

# Normalize the file path
normalizedPath = normalizePath(input_path)

# Remove leading slashes from the normalized file path
finalPath = removeLeadingSlashes(normalizedPath)

# Output the final modified file path
print(finalPath)
