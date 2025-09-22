def readInput():
    # Read the entire input from standard input and trim leading/trailing spaces
    return input().strip()

def normalizePath(inputPath):
    # Split the input path into components based on the separator
    parts = inputPath.split('/')
    normalized_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            # Ignore empty parts and current directory references
            continue
        elif part == '..':
            # Pop a part only if there's something to go back to
            if normalized_parts:
                normalized_parts.pop()
        else:
            # Add the valid part to the normalized path
            normalized_parts.append(part)
    
    # Join the normalized parts back into a path
    return '/' + '/'.join(normalized_parts)

def formatPath(normalizedPath):
    # Remove any leading slashes and ensure the path starts with a single slash
    return '/' + normalizedPath.lstrip('/')

def main():
    # Step 1: Read input path
    inputPath = readInput()
    
    # Step 2: Normalize the path
    normalizedPath = normalizePath(inputPath)
    
    # Step 3: Format the path
    formattedPath = formatPath(normalizedPath)

    # Output the final formatted path
    print(formattedPath)

# Checking if the script is running as the main program
if __name__ == "__main__":
    main()
