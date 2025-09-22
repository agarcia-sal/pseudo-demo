# START

# Read input from the user
userInput = input()

# Remove leading and trailing whitespace from the input
trimmedInput = userInput.strip()

# Normalize the path by eliminating redundant separators and up-level references
import os  # Importing os library to use its path normalization features
normalizedPath = os.path.normpath(trimmedInput)

# Replace multiple leading slashes with a single leading slash
# This can be done using regex or simple string manipulation
finalPath = '/' + normalizedPath.lstrip('/').replace('//', '/')

# Output the final normalized path
print(finalPath)

# END
