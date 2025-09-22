def normalize_file_path():
    # Step 1: Read the input
    inputPath = input().strip()  # Read input and remove any surrounding whitespace
    
    # Step 2: Normalize the path
    # Replace backslashes with forward slashes for POSIX compliance
    normalizedPath = inputPath.replace('\\', '/')
    
    # Step 3: Remove leading slashes
    # Use the lstrip method to replace leading slashes with a single leading slash
    finalPath = '/' + normalizedPath.lstrip('/')

    # Step 4: Print the resulting path
    print(finalPath)

# Main execution
normalize_file_path()
