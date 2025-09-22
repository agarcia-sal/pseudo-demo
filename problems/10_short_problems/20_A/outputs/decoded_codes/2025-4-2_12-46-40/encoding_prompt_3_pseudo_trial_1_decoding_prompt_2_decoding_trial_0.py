def main():
    # Read input data from standard input (console)
    rawFilePath = input()

    # Normalize the path to a standard format
    normalizedPath = NormalizePath(rawFilePath)

    # Print the adjusted normalized path
    print(normalizedPath)

def NormalizePath(inputPath):
    # Remove leading slashes from the path
    adjustedPath = RemoveLeadingSlashes(inputPath)

    # Return the normalized path
    return adjustedPath

def RemoveLeadingSlashes(path):
    # Replace multiple leading slashes with a single slash
    return ReplaceMultipleLeadingSlashesWithSingleSlash(path)

def ReplaceMultipleLeadingSlashesWithSingleSlash(path):
    # Use a regular expression to perform the replacement
    import re
    return re.sub(r'^/+','/', path)

# Start the program
if __name__ == "__main__":
    main()
