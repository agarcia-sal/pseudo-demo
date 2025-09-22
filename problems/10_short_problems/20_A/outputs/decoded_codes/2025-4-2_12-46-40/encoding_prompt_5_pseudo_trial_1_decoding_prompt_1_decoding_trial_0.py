def ReadInput():
    # Get the path from standard input and remove excess whitespace
    inputPath = input().strip()  # Using .strip() to trim whitespace
    return inputPath

def NormalizePath(path):
    # Normalize the file path to remove any redundant separators and up-level references
    normalizedPath = remove_reductions_from_path(path)  # Assume this is a defined function
    return normalizedPath

def EnsureSingleLeadingSlash(path):
    # If the path starts with one or more slashes 
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjustedPath = path.lstrip('/')  # Remove leading slashes
        adjustedPath = '/' + adjustedPath  # Add a single leading slash
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

# Call Main to execute the program
Main()
