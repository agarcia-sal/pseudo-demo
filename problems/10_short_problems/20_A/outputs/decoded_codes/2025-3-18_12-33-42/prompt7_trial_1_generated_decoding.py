def processInputPath():
    # Initialize inputPath as a string to hold the raw input from the user.
    inputPath = input().strip()
    
    # Normalize the input path to a standard format.
    # This is done using the replace method to simplify multiple slashes.
    # We first replace multiple slashes with a single slash, starting with '//' and going to the end of the string.
    while '//' in inputPath:
        inputPath = inputPath.replace('//', '/')
    
    # Replace leading slashes with a single leading slash if there are multiple.
    # We will use lstrip to remove leading slashes in the normalized path.
    normalizedPath = inputPath.lstrip('/')
    
    # Ensure that we only have one leading slash
    if normalizedPath and not normalizedPath.startswith('/'):
        normalizedPath = '/' + normalizedPath

    # Output the final processed path
    print(normalizedPath)

# This is the point where the function will be executed
processInputPath()
