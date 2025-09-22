# Begin program

def normalize_path(inputPath):
    """
    This function transforms the file path to a standard format.
    Implementation details depend on specific requirements for normalization.
    For demonstration, it will convert backslashes to forward slashes and 
    ensure no duplicate slashes appear in the path (except as needed).
    """
    # Replace backslashes with forward slashes for normalization
    normalized = inputPath.replace("\\", "/")
    # Remove any extra slashes from the normalized path
    # Splitting by slashes and joining ensures no duplicates
    normalized = '/'.join(filter(None, normalized.split('/')))
    return normalized

def replace_leading_slashes(path):
    """
    This function replaces sequences of leading slashes at the start of the path
    with a single leading slash.
    """
    # While the path starts with one or more slashes
    while path.startswith('/'):
        # Remove the leading slash
        path = path[1:]
    # Add a single leading slash back to the path
    return '/' + path if path else '/'

# Main execution starts here
inputPath = input().strip()  # Read input and remove leading/trailing whitespace

# Normalize the file path
normalizedPath = normalize_path(inputPath)

# Replace leading slashes in the normalized path with a single slash
finalPath = replace_leading_slashes(normalizedPath)

# Output the final normalized path
print(finalPath)

# End program
