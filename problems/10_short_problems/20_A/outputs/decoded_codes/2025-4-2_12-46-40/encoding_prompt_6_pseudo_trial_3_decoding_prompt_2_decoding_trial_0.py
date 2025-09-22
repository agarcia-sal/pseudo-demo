import os  # Importing os for path normalization

# Read input from standard input and remove any leading/trailing whitespace
inputString = input()
trimmedInputString = inputString.strip()

# Normalize the path, converting it to a standard format
normalizedPath = os.path.normpath(trimmedInputString)

# Replace any sequence of leading slashes with a single slash
updatedPath = normalizedPath.lstrip('/')

# Output the final transformed path
print('/' + updatedPath if updatedPath else updatedPath)
