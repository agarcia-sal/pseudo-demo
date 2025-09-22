def processInputPath():
    # Read input from standard input and remove leading/trailing whitespace
    inputPath = input().strip()
    
    # Normalize the path to ensure consistent formatting
    normalizedPath = normalizePath(inputPath)
    
    # Remove any leading slashes from the normalized path and ensure a single leading slash
    finalPath = removeLeadingSlashes(normalizedPath)
    
    # Print the final processed path
    print(finalPath)

def normalizePath(path):
    # Normalize the input path to a standard format using forward slashes
    return path.replace('\\', '/')  # Replace backslashes with forward slashes

def removeLeadingSlashes(path):
    import re
    # Use regular expression to replace multiple leading slashes with a single slash
    return re.sub(r'^/+','/', path)  # Replace one or more leading slashes with a single slash
