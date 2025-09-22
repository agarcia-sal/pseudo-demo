import re

def main():
    # Read input from standard input
    rawInput = input()
    
    # Normalize the file path to remove any redundant separators
    normalizedPath = normalize_path(rawInput)

    # Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
    finalPath = remove_leading_slashes(normalizedPath, 1)

    # Output the final formatted file path
    print(finalPath)

def normalize_path(input):
    # Normalize the file path (for example, resolving relative paths, removing unnecessary separators)
    # Here we implement a basic normalization (for demonstration purposes)
    return re.sub(r'/+', '/', input.strip())

def remove_leading_slashes(path, retainCount):
    # Replace multiple leading slashes with a single slash
    if len(path) == 0:
        return path
    leading_slashes = len(path) - len(path.lstrip('/'))
    if leading_slashes > retainCount:
        return '/' + path.lstrip('/')
    return path.lstrip('/')

if __name__ == "__main__":
    main()
