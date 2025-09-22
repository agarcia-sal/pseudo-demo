def NormalizePath(pathString):
    # This function should contain logic for normalizing the path string
    # For example, remove redundant slashes and resolve "." and ".."
    # Placeholder implementation (actual normalization logic is needed)
    normalized_path = pathString.replace("//", "/").strip()
    return normalized_path

def RemoveLeadingSlashes(pathString):
    # Removes leading slashes and returns the modified path
    return pathString.lstrip('/')

# Main execution starts here
rawPath = input()  # Read input from standard input

# Normalize the path
normalizedPath = NormalizePath(rawPath)

# Remove leading slashes from the normalized path
finalPath = RemoveLeadingSlashes(normalizedPath)

# Print the resulting path
print(finalPath)
