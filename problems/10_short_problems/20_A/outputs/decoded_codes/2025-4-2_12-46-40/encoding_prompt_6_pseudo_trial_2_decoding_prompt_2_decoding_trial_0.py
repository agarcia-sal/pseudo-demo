def normalize_path(inputPath):
    # This function transforms the file path to a standard format
    # (Implementation details depend on specific requirements for normalization)
    # For demonstration purposes, let's assume normalization means replacing backslashes with forward slashes
    return inputPath.replace("\\", "/")

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash

# BEGIN PROGRAM

# Read input from standard input and remove extra spaces
inputPath = input().strip()

# Normalize the file path
normalizedPath = normalize_path(inputPath)

# Replace any sequence of leading slashes with a single slash
finalPath = replace_leading_slashes(normalizedPath)

# Output the final normalized path
print(finalPath)

# END PROGRAM
