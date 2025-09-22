import posixpath
import re

def normalizeAndCleanPath():
    # Read a path from standard input
    readPath = input()
    
    # Normalize the path by removing any redundant separators
    normalizedPath = normalizePath(readPath)
    
    # Clean up the path to ensure it starts with a single forward slash
    cleanedPath = replaceMultipleLeadingSlashesWithSingleSlash(normalizedPath)
    
    # Print the cleaned path
    print(cleanedPath)

def normalizePath(inputPath):
    # Normalize the input path to remove any redundant separators
    return posixpath.normpath(inputPath)

def replaceMultipleLeadingSlashesWithSingleSlash(inputPath):
    # Remove multiple leading slashes, keeping only one
    return regularExpressionReplace(inputPath)

def regularExpressionReplace(inputPath):
    # Use a regular expression to replace leading slashes
    return re.sub('^/+', '/', inputPath)

# Call the main function to execute the path normalization and cleaning
normalizeAndCleanPath()
