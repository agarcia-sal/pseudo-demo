import os

def normalizeFilePath():
    # Step 1: Read the file path from standard input and strip extra spaces
    filePath = input().strip()

    # Step 2: Normalize the file path using system path conventions
    normalizedPath = os.path.normpath(filePath)

    # Step 3: Remove leading slashes
    # Replace multiple leading slashes with a single slash
    if normalizedPath.startswith('/'):
        finalPath = '/' + normalizedPath.lstrip('/')
    else:
        finalPath = normalizedPath

    # Step 4: Output the result
    print(finalPath)

# Call the normalizeFilePath function
normalizeFilePath()
