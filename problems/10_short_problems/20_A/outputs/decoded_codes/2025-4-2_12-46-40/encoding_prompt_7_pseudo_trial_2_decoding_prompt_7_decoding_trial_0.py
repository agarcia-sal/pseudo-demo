import re

def processInputPath():
    # Read input from standard input and remove leading/trailing whitespace
    inputPath = input().strip()

    # Normalize the path to ensure consistent formatting
    normalizedPath = normalizePath(inputPath)

    # Remove any leading slashes from the normalized path and ensure a single leading slash
    finalPath = removeLeadingSlashes(normalizedPath)

    # Print the final processed path
    print(finalPath)

def normalizePath(path):
    # Normalize the input path to a standard format using forward slashes
    # Replace backslashes with forward slashes (common in Windows paths)
    return path.replace('\\', '/')

def removeLeadingSlashes(path):
    # Use regular expression to replace multiple leading slashes with a single slash
    return re.sub(r'^/+','/', path)

# Test the functions with sample input
if __name__ == "__main__":
    processInputPath()
