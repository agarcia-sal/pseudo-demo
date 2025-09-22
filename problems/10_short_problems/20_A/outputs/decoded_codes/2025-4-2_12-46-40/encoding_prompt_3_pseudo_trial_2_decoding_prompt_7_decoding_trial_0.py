def main():
    # Read input from standard input
    rawPath = input()  # Receive the raw path string
    
    # Normalize the path
    normalizedPath = NormalizePath(rawPath)
    
    # Remove leading slashes from the normalized path
    finalPath = RemoveLeadingSlashes(normalizedPath)
    
    # Print the resulting path
    print(finalPath)


def NormalizePath(pathString):
    """
    Normalize the path by replacing multiple consecutive slashes with a single slash.
    This helps in ensuring that the path follows a proper format.
    """
    # Replace multiple slashes with a single slash
    normalized_path = '/'.join(segment for segment in pathString.split('/') if segment)
    return '/' + normalized_path if normalized_path else '/'


def RemoveLeadingSlashes(pathString):
    """
    Remove any leading slashes at the start of the string, ensuring the path starts with a single slash.
    """
    # Remove leading slashes by finding the path without leading slashes
    return '/' + pathString.lstrip('/')


# Call the main function to execute the code
if __name__ == "__main__":
    main()
