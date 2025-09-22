import posixpath
import re

def processInputPath():
    # Read the input from standard input and eliminate leading/trailing whitespace
    inputPath = input().strip()
    
    # Normalize the path to ensure it's in a canonical format
    normalizedPath = posixpath.normpath(inputPath)
    
    # Substitute any leading slashes with a single slash
    finalPath = re.sub(r'^/+', '/', normalizedPath)
    
    # Output the final processed path
    print(finalPath)

# Call the function to execute when the script runs
processInputPath()
