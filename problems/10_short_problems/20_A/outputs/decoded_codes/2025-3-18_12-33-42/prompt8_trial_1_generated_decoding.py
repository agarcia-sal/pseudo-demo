import re

def NormalizeFilePath():
    # Step 1: Read input from the user
    rawPath = input()
    
    # Step 2: Normalize the input path
    normalizedPath = NormalizePath(rawPath)

    # Step 3: Clean up the normalized path by ensuring it does not start with multiple slashes
    cleanedPath = RemoveLeadingSlashes(normalizedPath)

    # Step 4: Output the final cleaned path
    print(cleanedPath)


def NormalizePath(path):
    # Replace any backslashes with forward slashes
    return ReplaceBackslashesWithForwardslashes(path)


def RemoveLeadingSlashes(path):
    # Use a regular expression to replace any occurrences of multiple leading slashes with a single slash
    return ReplaceMultipleLeadingSlashesWithSingleSlash(path)


def ReplaceBackslashesWithForwardslashes(path):
    # This function takes a path and replaces all backslashes with forward slashes
    return path.replace('\\', '/')


def ReplaceMultipleLeadingSlashesWithSingleSlash(path):
    # This function takes a path and uses a regular expression to replace any leading slashes
    # that appear more than once at the beginning of the string with just one leading slash
    return re.sub(r'^/+', '/', path)


# To run the function
NormalizeFilePath()
