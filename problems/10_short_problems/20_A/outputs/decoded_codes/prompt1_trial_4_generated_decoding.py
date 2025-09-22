def main():
    # Read the input from the standard input
    rawInput = input()

    # Normalize the input path by removing any redundant separators and up-level references
    normalizedPath = normalize_path(rawInput)

    # Replace any leading slashes with a single slash
    finalPath = replace_leading_slashes(normalizedPath)

    # Output the processed path
    print(finalPath)

def normalize_path(inputPath):
    # Normalize the path by converting it to use the appropriate format for the operating system
    return normal_path_using_system_rules(inputPath)

def replace_leading_slashes(path):
    # If the path starts with multiple slashes, replace them with a single slash
    if path.startswith('/'):
        return '/' + rest_of_path(path)
    else:
        return path

def rest_of_path(path):
    # Return the path excluding the leading slashes
    return path.lstrip('/')

# This ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()
