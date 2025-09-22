def NormalizeFilePath(rawFilePath):
    # Trim whitespace from the input
    trimmedFilePath = REMOVE_WHITESPACE(rawFilePath)
    
    # Normalize the file path by removing unnecessary segments
    normalizedFilePath = REMOVE_REDUNDANT_PATH_SEGMENTS(trimmedFilePath)
    
    # Ensure the normalized path starts with a single forward slash
    finalFilePath = ENSURE_SINGLE_LEADING_SLASH(normalizedFilePath)
    
    return finalFilePath

def REMOVE_WHITESPACE(filePath):
    # Remove leading and trailing whitespace from the filePath
    return filePath.strip()

def REMOVE_REDUNDANT_PATH_SEGMENTS(filePath):
    # Replace multiple sequential slashes (//) with a single slash (/)
    while '//' in filePath:
        filePath = filePath.replace('//', '/')
    return filePath

def ENSURE_SINGLE_LEADING_SLASH(filePath):
    if filePath.startswith('/'):
        return filePath  # Already has a leading slash
    else:
        return '/' + filePath  # Add a leading slash

# Read the input from the standard input
userInput = input()

# Normalize the file path
resultPath = NormalizeFilePath(userInput)

# Print the final normalized file path
print(resultPath)
