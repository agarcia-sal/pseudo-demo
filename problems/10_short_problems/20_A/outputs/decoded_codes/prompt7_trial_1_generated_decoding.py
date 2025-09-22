import posixpath  # Importing the posixpath library for path normalization
import re  # Importing regex library for string manipulation

def processFilePath(inputFilePath):
    # Normalize the input file path
    normalizedPath = normalizePath(inputFilePath)
    
    # Remove leading slashes from the normalized path
    resultPath = removeLeadingSlashes(normalizedPath)
    
    # Print the final processed path
    print(resultPath)

def normalizePath(path):
    # Normalize the given path to a standard format using posixpath.normpath
    return posixpath.normpath(path)

def removeLeadingSlashes(path):
    # Substitute leading slashes with a single leading slash using regex
    return re.sub(r'^/+', '/', path)

# Main execution starts here
inputPath = input()  # Read the input file path from standard input
processFilePath(inputPath)  # Process the input file path
