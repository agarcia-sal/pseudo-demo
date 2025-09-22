def normalizePath(filePath):
    # Implementation that handles path normalization
    # This may include removing '.', '..', and multiple slashes
    # Here we will use os.path.normpath for demonstration
    import os
    normalizedPath = os.path.normpath(filePath)
    return normalizedPath

def removeExtraLeadingSlashes(filePath):
    # Implementation that ensures the path starts with a single slash
    # This replaces leading slashes with a single one
    while filePath.startswith('/'):
        filePath = filePath[1:]
    return '/' + filePath

# Start of the program
rawFilePath = input()  # Read input from standard input

# Normalize the file path
normalizedFilePath = normalizePath(rawFilePath)

# Ensure the path starts with a single forward slash
if normalizedFilePath.startswith('/'):
    resultFilePath = removeExtraLeadingSlashes(normalizedFilePath)
else:
    resultFilePath = normalizedFilePath  # Keep as is if there are no leading slashes

# Print the final result
print(resultFilePath)
