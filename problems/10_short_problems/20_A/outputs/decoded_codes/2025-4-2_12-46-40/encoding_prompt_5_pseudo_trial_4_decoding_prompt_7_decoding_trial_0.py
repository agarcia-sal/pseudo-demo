def main():
    # Read the entire input from standard input (expected to be a file path)
    rawPath = input()

    # Normalize the file path by removing redundant path separators
    normalizedPath = normalize_path(rawPath)

    # Output the cleaned path
    print(normalizedPath)

def normalize_path(pathString):
    # Use the built-in functionality to normalize the path
    # This is a placeholder for internal standardization logic
    cleanedPath = standardize(pathString)

    # Replace multiple leading slashes with a single slash at the start of the path
    cleanedPath = replace_leading_slashes(cleanedPath)
    
    return cleanedPath

def standardize(pathString):
    # This function can include logic to handle platform-specific path normalization
    # For simplifying, we return the path as is. In real scenarios,
    # you would convert backslashes to slashes and perform other normalization.
    return pathString  

def replace_leading_slashes(cleanedPath):
    # Check if the path starts with two or more slashes and replace them
    while cleanedPath.startswith('//'):
        cleanedPath = remove_one_slash_from_start(cleanedPath)
    
    return cleanedPath

def remove_one_slash_from_start(path):
    # Remove one leading slash from the given path
    return path[1:] if path else path  # Ensure we don't remove from an empty string

# Entry point of the script
if __name__ == "__main__":
    main()
