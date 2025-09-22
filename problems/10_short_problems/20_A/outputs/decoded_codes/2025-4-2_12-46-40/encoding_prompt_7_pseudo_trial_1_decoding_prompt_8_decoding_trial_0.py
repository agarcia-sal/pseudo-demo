def normalize(inputPath):
    import os
    # Normalize the file path by resolving any '..' or '.' references
    return os.path.normpath(inputPath)

def normalizeAndPrintPath():
    # Read input from standard input and remove any leading/trailing whitespace
    inputPath = input().strip()

    # Normalize the file path to remove unnecessary components
    normalizedPath = normalize(inputPath)

    # Replace any leading slashes with a single slash
    finalPath = normalizedPath.lstrip('/').replace('//', '/')

    # Output the final formatted path
    print('/' + finalPath)

# Run the function
normalizeAndPrintPath()
