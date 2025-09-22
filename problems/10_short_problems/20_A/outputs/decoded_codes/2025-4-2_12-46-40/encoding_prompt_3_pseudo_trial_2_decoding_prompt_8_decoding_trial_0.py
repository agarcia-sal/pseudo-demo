def main():
    # Read input from standard input
    rawPath = input()

    # Normalize the path
    normalizedPath = NormalizePath(rawPath)

    # Remove leading slashes from the normalized path
    finalPath = RemoveLeadingSlashes(normalizedPath)

    # Print the resulting path
    print(finalPath)


def NormalizePath(pathString):
    # This function would contain logic to normalize the path
    # For simplicity, we'll replace multiple slashes with a single one and remove trailing slashes
    import os
    return os.path.normpath(pathString)


def RemoveLeadingSlashes(pathString):
    # Replace any leading slashes at the start of the string with a single slash
    return '/' + pathString.lstrip('/')


if __name__ == "__main__":
    main()
