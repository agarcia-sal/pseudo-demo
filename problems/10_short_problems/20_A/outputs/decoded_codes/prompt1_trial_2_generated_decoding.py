# Main part of the program
rawInput = input()  # Read input from the standard input
normalizedPath = NormalizePath(rawInput)  # Normalize the file path to standard format
cleanedPath = CleanUpPath(normalizedPath)  # Clean up the path to ensure it starts with a single forward slash
print(cleanedPath)  # Output the finalized cleaned path

def NormalizePath(inputPath):
    # Replace any backslashes with forward slashes
    return inputPath.replace('\\', '/')  # Replaces backslashes with forward slashes

def CleanUpPath(path):
    # Remove any leading slashes, leaving only one if present
    if path.startswith('//'):
        return '/' + path.lstrip('/')  # Ensures only one leading slash is kept
    else:
        return path  # Returns the path as is if it does not start with multiple slashes
