import os
import re

def main():
    # Read input from user
    inputPath = input()
    
    # Normalize the input path to remove redundant elements
    normalizedPath = os.path.normpath(inputPath)
    
    # Replace leading slashes in normalizedPath with a single slash
    finalPath = re.sub(r'^/+', '/', normalizedPath)
    
    # Print the final formatted path to standard output
    print(finalPath)

# Call the main function
main()
