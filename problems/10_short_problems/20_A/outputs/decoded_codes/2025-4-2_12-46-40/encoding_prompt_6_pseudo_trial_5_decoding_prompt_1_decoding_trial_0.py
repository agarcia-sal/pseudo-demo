def useRegularExpressionToReplaceLeadingSlashes(path):
    import re
    # Substitute the start of the string which matches one or more slashes with a single slash
    modifiedPath = re.sub(r'^/+','/', path)
    return modifiedPath

def removeLeadingSlashes(path):
    # Use regular expression to replace leading slashes with a single slash
    modifiedPath = useRegularExpressionToReplaceLeadingSlashes(path)
    return modifiedPath

def normalizePath(path):
    # Remove leading slashes from the path
    cleanedPath = removeLeadingSlashes(path)
    return cleanedPath

# Read a string of file path data from standard input
inputPath = input()

# Normalize the file path by removing any excessive slashes
normalizedPath = normalizePath(inputPath)

# Print the result to standard output
print(normalizedPath)
