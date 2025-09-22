import os

def NormalizeFilePathFromInput():
    # Read the entire input from the standard input stream
    inputPath = input()
    
    # Normalize the input path using the Normalize function
    normalizedPath = Normalize(inputPath)
    
    # Adjust the normalized path to ensure it does not start with multiple leading slashes
    finalPath = normalizedPath.lstrip('/')
    
    # Output the final normalized path
    print(finalPath)

def Normalize(inputPath):
    # This function applies normalization to the input path
    # by converting backslashes to slashes and removing redundant separators
    
    # Normalize the path using os.path.normpath which applies file system rules
    normalized_path = os.path.normpath(inputPath.replace('\\', '/'))
    
    return normalized_path

# Run the normalization function
NormalizeFilePathFromInput()
