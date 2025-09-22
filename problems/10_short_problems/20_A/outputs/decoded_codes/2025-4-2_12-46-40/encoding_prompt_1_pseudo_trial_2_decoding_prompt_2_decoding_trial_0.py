import os

# Start Program

# Get Input
inputString = input().strip()  # Read input and remove leading/trailing whitespace

# Normalize Path
def normalize_path(path):
    return os.path.normpath(path)  # Normalize the file path

normalizedPath = normalize_path(inputString)

# Clean Path
def clean_path(path):
    while path.startswith('/'):
        path = path[1:]  # Remove leading slashes
    return '/' + path  # Add a single leading slash

cleanedPath = clean_path(normalizedPath)

# Output Result
print(cleanedPath)

# End Program
