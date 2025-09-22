import os

def ReadInput():
    inputPath = input().strip()
    return inputPath

def NormalizePath(path):
    normalizedPath = os.path.normpath(path)
    return normalizedPath

def EnsureSingleLeadingSlash(path):
    if path.startswith('/'):
        adjustedPath = '/' + path.lstrip('/')
    else:
        adjustedPath = '/' + path
    return adjustedPath

def Main():
    userInput = ReadInput()
    normalizedInput = NormalizePath(userInput)
    finalPath = EnsureSingleLeadingSlash(normalizedInput)
    print(finalPath)

Main()
