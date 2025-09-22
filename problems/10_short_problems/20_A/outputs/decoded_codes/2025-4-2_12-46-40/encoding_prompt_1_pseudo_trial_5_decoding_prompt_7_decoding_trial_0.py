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
    # Split the path into components and handle '.' and '..'
    components = path.split('/')
    stack = []

    for component in components:
        if component == '' or component == '.':
            # Skip empty components or current directory indicators
            continue
        elif component == '..':
            # Go up one directory, if possible
            if stack:
                stack.pop()
        else:
            # Normal path component, add to the stack
            stack.append(component)

    # Join the components back into a normalized path
    simplifiedPath = '/'.join(stack)
    
    # If stack is empty, return root path
    return simplifiedPath if simplifiedPath else '/'

def ReplaceLeadingSlashesWithOne(path):
    # Replace all leading slashes with a single slash
    return '/' + path.lstrip('/')

# Call the main function to execute the program
if __name__ == "__main__":
    main()
