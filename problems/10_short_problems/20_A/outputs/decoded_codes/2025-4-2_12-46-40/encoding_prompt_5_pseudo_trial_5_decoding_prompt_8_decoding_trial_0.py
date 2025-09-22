import os

def normalizeFilePath():
    # STEP 1: Read the file path from standard input
    filePath = input().strip()  # Remove extra spaces

    # STEP 2: Normalize the file path
    normalizedPath = os.path.normpath(filePath)  # Normalize using system path conventions

    # STEP 3: Remove leading slashes
    finalPath = normalizedPath.lstrip('/')  # Remove leading slashes
    if finalPath:  # If finalPath is not empty, add a leading slash
        finalPath = '/' + finalPath

    # STEP 4: Output the result
    print(finalPath)

# Example call to the function (comment this line for real use)
# normalizeFilePath()
