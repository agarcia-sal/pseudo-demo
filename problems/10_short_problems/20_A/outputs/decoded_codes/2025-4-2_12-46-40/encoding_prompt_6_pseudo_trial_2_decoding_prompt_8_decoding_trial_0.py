def main():
    # Read input from standard input and remove extra spaces
    inputPath = input().strip()

    # Normalize the file path
    normalizedPath = normalize_path(inputPath)

    # Replace any sequence of leading slashes with a single slash
    finalPath = replace_leading_slashes(normalizedPath)

    # Output the final normalized path
    print(finalPath)

def normalize_path(inputPath):
    # This function transforms the file path to a standard format
    # Here we assume normalization means converting to absolute path and removing unnecessary elements
    import os
    return os.path.normpath(inputPath)

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]
    return '/' + path if path else '/'

if __name__ == "__main__":
    main()
