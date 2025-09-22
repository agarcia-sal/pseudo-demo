import posixpath
import re

def normalizeAndCleanPath():
    readPath = input()

    normalizedPath = normalizePath(readPath)
    
    cleanedPath = replaceMultipleLeadingSlashesWithSingleSlash(normalizedPath)

    print(cleanedPath)

def normalizePath(inputPath):
    return posixpath.normpath(inputPath)

def replaceMultipleLeadingSlashesWithSingleSlash(inputPath):
    return regularExpressionReplace(inputPath)

def regularExpressionReplace(inputPath):
    return re.sub(r'^/+', '/', inputPath)

# You would typically call the main function if this is the entry point
# normalizeAndCleanPath()
