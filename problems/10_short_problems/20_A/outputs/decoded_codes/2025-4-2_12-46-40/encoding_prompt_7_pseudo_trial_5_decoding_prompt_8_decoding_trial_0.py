def normalizeFilePathAndPrint(inputString):
    # REMOVE leading and trailing whitespace from inputString
    cleanedInput = inputString.strip()
    
    # NORMALIZE the file path using a standard format
    normalizedPath = cleanedInput.replace('\\', '/')
    
    # REPLACE any occurrences of multiple leading slashes with a single leading slash
    while '//' in normalizedPath:
        normalizedPath = normalizedPath.replace('//', '/')
    
    # PRINT the formatted file path
    print(normalizedPath)

# MAIN EXECUTION BLOCK
inputString = input()
normalizeFilePathAndPrint(inputString)
