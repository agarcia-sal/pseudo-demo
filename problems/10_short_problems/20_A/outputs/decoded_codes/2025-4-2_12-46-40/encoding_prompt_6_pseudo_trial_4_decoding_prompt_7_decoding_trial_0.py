def ReplaceMultipleLeadingSlashesWithOne(path):
    # This function replaces multiple leading slashes with a single slash
    while path.startswith('/'):
        path = path[1:]  # Remove the first character (a leading slash)
    return '/' + path  # Return with a single leading slash

def NormalizePath(inputPath):
    # This function normalizes the given file path
    # Split the path by '/', remove empty segments, and join back
    segments = inputPath.split('/')
    normalized_segments = [segment for segment in segments if segment]  # Filter out empty segments
    return '/'.join(normalized_segments)  # Join segments back with a single slash

def Main():
    # Step 1: Read input from the standard input (user)
    userInput = input()  # Assume user will provide a file path
    
    # Step 2: Normalize the input file path
    normalizedPath = NormalizePath(userInput)
    
    # Step 3: Adjust leading slashes
    if normalizedPath.startswith('/'):
        normalizedPath = ReplaceMultipleLeadingSlashesWithOne(normalizedPath)

    # Step 4: Output the final normalized path
    print(normalizedPath)  # Display the modified file path to the user

# Execute the main function
if __name__ == "__main__":
    Main()
