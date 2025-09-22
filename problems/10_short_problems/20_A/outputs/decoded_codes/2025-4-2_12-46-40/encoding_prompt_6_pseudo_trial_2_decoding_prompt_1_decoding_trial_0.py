def normalize_path(inputPath):
    # This function transforms the file path to a standard format
    # Implementation details depend on specific requirements for normalization
    return normalized_path_version(inputPath)  # Placeholder for actual implementation

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash

# BEGIN PROGRAM
inputPath = input().strip()  # Read input and remove leading/trailing whitespace
normalizedPath = normalize_path(inputPath)  # Normalize the path
finalPath = replace_leading_slashes(normalizedPath)  # Replace leading slashes with a single slash
print(finalPath)  # Output the final normalized path
# END PROGRAM
