def normalizeAndPrintPath():
    # Read input from standard input and remove any leading/trailing whitespace
    inputPath = input().strip()

    # Normalize the file path to remove unnecessary components
    normalizedPath = normalize(inputPath)

    # Replace any leading slashes with a single slash
    finalPath = normalizedPath.lstrip('/')

    # Output the final formatted path
    print(finalPath)

def normalize(inputPath):
    # Normalize the file path by converting it to a standard format
    # This could involve resolving any '..' or '.' references in the path
    import os
    return os.path.normpath(inputPath)
