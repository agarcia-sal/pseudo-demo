import os

def normalize_path(path):
    # Normalize the path to resolve any navigation symbols
    return os.path.normpath(path)

def main():
    # Step 1: Read input
    originalPath = input()
    trimmedPath = originalPath.strip()  # Remove extra spaces from both ends

    # Step 2: Normalize the file path
    normalizedPath = normalize_path(trimmedPath)

    # Step 3: Ensure the path starts with a single forward slash
    if normalizedPath.startswith('/'):
        finalPath = '/' + normalizedPath.lstrip('/')
    else:
        finalPath = '/' + normalizedPath

    # Step 4: Output the final result
    print(finalPath)

if __name__ == "__main__":
    main()
