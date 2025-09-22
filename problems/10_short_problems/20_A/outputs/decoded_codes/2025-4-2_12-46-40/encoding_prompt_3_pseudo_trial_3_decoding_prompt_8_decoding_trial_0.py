import os
import re

# Read input from the user
userInput = input()

# Remove leading and trailing whitespace from the input
trimmedInput = userInput.strip()

# Normalize the path by eliminating redundant separators and up-level references
normalizedPath = os.path.normpath(trimmedInput)

# Replace multiple leading slashes with a single leading slash
finalPath = re.sub(r'^/{2,}', '/', normalizedPath)

# Output the final normalized path
print(finalPath)
