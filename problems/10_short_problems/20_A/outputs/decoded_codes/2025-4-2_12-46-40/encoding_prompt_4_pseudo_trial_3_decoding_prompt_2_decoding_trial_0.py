import re

# Read input from standard input
rawInput = input()

# Normalize the file path to remove any redundant separators
def normalize_path(input):
    # Convert the input to a normalized form (e.g., resolve relative paths, remove unnecessary separators)
    return input.replace('//', '/').strip()

# Use a regular expression to ensure the path starts with a single '/' if it contains any leading slashes
def remove_leading_slashes(path, retainCount):
    # Replace multiple leading slashes with a single slash
    return re.sub(r'^/+', '/', path)

# Main execution flow
normalizedPath = normalize_path(rawInput)
finalPath = remove_leading_slashes(normalizedPath, 1)

# Output the final formatted file path
print(finalPath)
