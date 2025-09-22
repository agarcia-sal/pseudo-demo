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
    # Placeholder for actual normalization logic
    # Replace redundant path components to simplify the path
    # This function would typically perform operations like resolving '..' and '.'
    return path  # Implement normalization logic here as needed

def ReplaceLeadingSlashesWithOne(path):
    # Replace all leading slashes with a single slash
    while path.startswith('/'):
        path = path[1:]
    return '/' + path

# Execute the main function
if __name__ == "__main__":
    main()
