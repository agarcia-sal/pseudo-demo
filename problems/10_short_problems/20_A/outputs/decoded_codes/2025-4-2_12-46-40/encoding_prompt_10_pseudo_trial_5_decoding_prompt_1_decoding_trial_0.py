# Define Main Procedure:
def normalize_path():
    
    # Read Input:
    inputPath = input()
    
    # Clean the Input Path:
    normalizedPath = inputPath.replace('//', '/').strip()  # Basic normalization example; you can expand this logic as needed

    # Substitute Leading Slashes:
    if normalizedPath.startswith('/'):
        finalPath = '/' + normalizedPath.lstrip('/')
    else:
        finalPath = normalizedPath.lstrip('/')
    
    # Output the Result:
    print(finalPath)

# Call the procedure to execute
normalize_path()
