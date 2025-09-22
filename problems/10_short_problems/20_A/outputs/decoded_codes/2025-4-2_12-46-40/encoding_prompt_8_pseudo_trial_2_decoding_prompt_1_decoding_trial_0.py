def main():
    # Step 1: Read the input file path from standard input
    userInput = input()
    
    # Step 2: Normalize the input path
    normalizedPath = NormalizePath(userInput)
    
    # Step 3: Ensure the normalized path starts with a single '/'
    finalPath = ReplaceMultipleLeadingSlashes(normalizedPath)
    
    # Step 4: Print the final normalized path
    print(finalPath)

def NormalizePath(inputPath):
    # This function would implement normalization by retaining relevant parts of the path
    # For demonstration purposes, we will assume it returns the inputPath cleaned up.
    # In a real implementation, this would likely involve more logic.
    # Placeholder for normalization logic
    normalizedInputPath = inputPath  # Placeholder, adjust as needed
    return normalizedInputPath

def ReplaceMultipleLeadingSlashes(path):
    # Check for slashes at the start of the path
    if path.startswith('/'):
        # Replace any occurrence of multiple leading slashes with a single slash
        while path.startswith('//'):  # while there are multiple leading slashes
            path = path.replace('//', '/', 1)  # Replace two slashes with one, limit to first occurrence
        return path
    else:
        return '/' + path  # Prepend a single slash if none exists

# Entry point of the program
main()
