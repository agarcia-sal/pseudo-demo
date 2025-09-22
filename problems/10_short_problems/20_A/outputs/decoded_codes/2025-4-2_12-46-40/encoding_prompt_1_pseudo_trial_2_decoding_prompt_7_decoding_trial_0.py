import os

def normalize_path(path):
    """Normalize the given file path, resolving any relative path components."""
    return os.path.normpath(path)

def clean_path(path):
    """Clean the file path by ensuring a single leading forward slash."""
    # Remove leading slashes and then add a single leading slash at the beginning
    return '/' + path.lstrip('/')

# Start Program
# Get Input
inputString = input().strip()  # Read input and remove any leading or trailing whitespace

# Normalize Path
normalizedPath = normalize_path(inputString)  # Normalize the file path

# Clean Path
cleanedPath = clean_path(normalizedPath)  # Clean the normalized path

# Output Result
print(cleanedPath)  # Print the cleaned file path

# End Program
