import posixpath

def NormalizeAndCleanPath(inputString):
    # Step 1: Normalize the input path using the posixpath library
    normalizedPath = posixpath.normpath(inputString)

    # Step 2: Remove any leading slashes from the normalized path
    cleanedPath = normalizedPath.lstrip('/')

    # Step 3: Return the cleaned path
    return cleanedPath

# Main process to read input and execute path normalization
inputString = input()  # Read input from standard input
finalPath = NormalizeAndCleanPath(inputString)  # Normalize and clean the path
print(finalPath)  # Print the final path
