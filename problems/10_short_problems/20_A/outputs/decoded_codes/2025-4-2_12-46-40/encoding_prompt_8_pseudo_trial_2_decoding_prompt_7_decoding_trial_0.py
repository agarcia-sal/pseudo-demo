def main():
    # Step 1: Read the input file path from standard input
    userInput = input()
    
    # Step 2: Normalize the input path
    # This means removing any redundant separators or up-level references
    normalizedPath = NormalizePath(userInput)
    
    # Step 3: Ensure the normalized path starts with a single '/'
    finalPath = ReplaceMultipleLeadingSlashes(normalizedPath)
    
    # Step 4: Print the final normalized path
    print(finalPath)

def NormalizePath(inputPath):
    # Split the input path into components while removing empty components
    parts = inputPath.split('/')
    # Remove unnecessary parts such as '.' and empty strings
    filteredParts = [part for part in parts if part and part != '.']
    # Handle up-level references by removing the last part if '..' is encountered
    resultParts = []
    for part in filteredParts:
        if part == '..':
            if resultParts:  # Only pop if there's something to pop
                resultParts.pop()
        else:
            resultParts.append(part)
    # Join the cleaned components back into a normalized path
    normalizedInputPath = '/'.join(resultParts)
    return normalizedInputPath

def ReplaceMultipleLeadingSlashes(path):
    # Check for multiple leading slashes
    if path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        return '/' + path.lstrip('/')
    else:
        # Prepend a single slash if none exists
        return '/' + path

# Run the main program
main()
