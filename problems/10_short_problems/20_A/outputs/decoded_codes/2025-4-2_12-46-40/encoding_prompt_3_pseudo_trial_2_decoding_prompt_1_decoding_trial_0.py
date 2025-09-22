def main():
    # Read input from standard input
    rawPath = input()  # This will receive the raw path string

    # Normalize the path
    normalizedPath = normalize_path(rawPath)

    # Remove leading slashes from the normalized path
    finalPath = remove_leading_slashes(normalizedPath)

    # Print the resulting path
    print(finalPath)

def normalize_path(pathString):
    # Replace the path with a normalized version
    # This is a placeholder for actual normalization logic
    return pathString  # Replace with actual normalization logic

def remove_leading_slashes(pathString):
    # Replace any leading slashes at the start of the string with a single slash
    return '/' + pathString.lstrip('/')

# Entry point of the program
if __name__ == "__main__":
    main()
