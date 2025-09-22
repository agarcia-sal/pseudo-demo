def normalize(path):
    # Replace backslashes with forward slashes
    return path.replace('\\', '/')

def replace_multiple_leading_slashes_with_single_slash(path):
    # Replace occurrences of one or more leading slashes at the start of path with a single slash
    return path.lstrip('/').rfind('/') + 1 * '/' + path.lstrip('/')

# Read a file path from standard input
inputPath = input()

# Normalize the input path to a standard format
normalizedPath = normalize(inputPath)

# Remove leading slashes from the normalized path, leaving only a single leading slash if it exists
cleanedPath = replace_multiple_leading_slashes_with_single_slash(normalizedPath)

# Output the final cleaned path
print(cleanedPath)
