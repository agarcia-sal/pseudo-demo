# Function to normalize the file path by replacing backslashes with forward slashes
def normalizePath(path):
    # Replace backslashes with forward slashes for normalization
    return path.replace('\\', '/')

# Function to remove leading slashes from the path
def removeLeadingSlashes(path):
    # Use lstrip to remove leading slashes, ensuring no more than one leading '/' remains
    return '/' + path.lstrip('/')

# Read input path from standard input
input_path = input()

# Normalize the file path
normalizedPath = normalizePath(input_path)

# Remove leading slashes from the normalized file path
finalPath = removeLeadingSlashes(normalizedPath)

# Output the final modified file path
print(finalPath)
