def readInput():
    # Read the entire input from standard input and remove leading/trailing spaces
    return input().strip()

def normalizePath(inputPath):
    # Normalize the path by removing redundant separators and up-level references
    # This is a basic implementation, actual logic may vary based on requirements
    parts = inputPath.split('/')
    normalized_parts = []
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if normalized_parts:
                normalized_parts.pop()
        else:
            normalized_parts.append(part)
    return '/'.join(normalized_parts)

def formatPath(normalizedPath):
    # Remove any leading slashes in the normalized path (except for the root path)
    return normalizedPath.lstrip('/')

def main():
    # Read input path
    inputPath = readInput()
    
    # Normalize the path
    normalizedPath = normalizePath(inputPath)
    
    # Format the path
    formattedPath = formatPath(normalizedPath)

    # Output the final formatted path
    print(formattedPath)

# Call the main function to execute the program
main()
