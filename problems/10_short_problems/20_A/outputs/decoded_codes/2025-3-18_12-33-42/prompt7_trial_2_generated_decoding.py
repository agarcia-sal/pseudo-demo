def normalizeFilePath():
    # Read input from standard input (keyboard or other source)
    inputPath = input()
    
    # Normalize the file path by removing redundant separators
    normalizedPath = normalizePath(inputPath)
    
    # Remove leading slashes and replace them with a single slash if present
    finalPath = replaceLeadingSlashes(normalizedPath)
    
    # Print the resulting file path
    print(finalPath)

def normalizePath(inputPath):
    # Normalize the input path format to remove redundant path separators
    # Split the path by "/" and filter out empty segments
    segments = inputPath.split("/")
    normalizedSegments = [seg for seg in segments if seg != ""]
    
    # Join the segments back together with a single "/"
    return "/".join(normalizedSegments)

def replaceLeadingSlashes(path):
    # Replace any occurrence of multiple leading slashes with a single slash
    while path.startswith("//"):
        path = path[1:]  # Remove the leading slash
    return "/" + path  # Ensure at least one leading slash

# Call the function to execute the normalization process
normalizeFilePath()
