def ReadInput():
    # Get the path from standard input and remove excess whitespace
    inputPath = input().strip()
    return inputPath

def NormalizePath(path):
    # Normalize the file path to remove any redundant separators and up-level references
    normalizedPath = REMOVE_REDUCTIONS_FROM_PATH(path)  # Placeholder function
    return normalizedPath

def EnsureSingleLeadingSlash(path):
    # If the path starts with one or more slashes
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjustedPath = '/' + path.lstrip('/')
    else:
        # Return the path as is since it already has a single slash
        adjustedPath = path
    return adjustedPath

def Main():
    # Read and clean the input path
    userInput = ReadInput()
    
    # Normalize the input path for standardization
    normalizedInput = NormalizePath(userInput)
    
    # Ensure the normalized path has a proper leading slash
    finalPath = EnsureSingleLeadingSlash(normalizedInput)
    
    # Output the final cleaned path
    print(finalPath)

# Call the main function to execute
Main()
