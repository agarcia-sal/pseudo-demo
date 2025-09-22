def main():
    # Read input from standard input
    rawFilePath = input()

    # Normalize the file path by removing trailing slashes and redundant elements
    normalizedFilePath = NormalizePath(rawFilePath)

    # Print the resulting normalized file path
    print(normalizedFilePath)

def NormalizePath(inputPath):
    # Remove surrounding whitespace from the input path
    trimmedPath = TrimWhitespace(inputPath)

    # Normalize the path to standard format (e.g., convert to POSIX path)
    normalizedPath = NormalizeFormat(trimmedPath)

    # Replace leading slash(es) with a single slash
    if normalizedPath.startswith('/'):
        normalizedPath = ReplaceLeadingSlashesWithOne(normalizedPath)

    return normalizedPath

def TrimWhitespace(path):
    # Remove whitespace from the beginning and end of the string
    return path.strip()

def NormalizeFormat(path):
    # Split the path into components, filter out empty components and current directory symbols, then join back
    components = path.split('/')
    normalizedComponents = [comp for comp in components if comp and comp != '.']
    
    # Handle '..' for parent directory traversal
    stack = []
    for comp in normalizedComponents:
        if comp == '..':
            if stack:
                stack.pop()  # Go up one directory
        else:
            stack.append(comp)

    # Create the normalized path
    simplifiedPath = '/' + '/'.join(stack)
    return simplifiedPath

def ReplaceLeadingSlashesWithOne(path):
    # Replace all leading slashes with a single slash
    while path.startswith('/'):
        path = path[1:]
    return '/' + path

# Call the main function to execute the program
if __name__ == "__main__":
    main()
