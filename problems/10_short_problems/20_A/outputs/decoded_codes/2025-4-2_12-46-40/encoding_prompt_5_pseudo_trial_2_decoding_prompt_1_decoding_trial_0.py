import os

def normalize_file_path():
    # Step 1: Read the input
    inputPath = input()
    
    # Step 2: Normalize the path
    normalizedPath = os.path.normpath(inputPath)

    # Step 3: Remove leading slashes
    if normalizedPath.startswith('/'):  # Check if there's at least one leading slash
        finalPath = '/' + normalizedPath.lstrip('/')
    else:
        finalPath = normalizedPath  # No leading slashes to remove

    # Step 4: Print the resulting path
    print(finalPath)

# Main execution
normalize_file_path()
