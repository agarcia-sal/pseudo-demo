def main():
    # Read the entire input from standard input (assumed to be a file path)
    rawPath = input()
    
    # Normalize the file path by removing redundant path separators
    normalizedPath = normalize_path(rawPath)

    # Output the cleaned path
    print(normalizedPath)

def normalize_path(pathString):
    # Use the built-in functionality to normalize the path
    cleanedPath = standardize(pathString)

    # Replace multiple leading slashes with a single slash at the start of the path
    cleanedPath = replace_leading_slashes(cleanedPath)
    
    return cleanedPath

def standardize(pathString):
    # This function would perform internal path normalization (like converting backslashes to slashes)
    # Here, we let it assume the shaping of the path based on the platform-specific requirements
    return pathString  # Placeholder for actual internal standardization logic

def replace_leading_slashes(cleanedPath):
    # Check if the path starts with one or more slashes
    # Replace all occurrences of multiple slashes at the beginning with a single slash
    while cleanedPath.startswith('//'):  # While it starts with two or more slashes
        cleanedPath = remove_one_slash_from_start(cleanedPath)
    
    return cleanedPath

def remove_one_slash_from_start(path):
    # Remove one leading slash from the given path
    return path[1:]

if __name__ == "__main__":
    main()
