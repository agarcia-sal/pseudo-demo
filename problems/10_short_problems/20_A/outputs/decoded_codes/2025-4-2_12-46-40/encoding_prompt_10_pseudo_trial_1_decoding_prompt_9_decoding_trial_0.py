import os
import re

# Read input from the user
inputString = input().strip()  # Removes leading and trailing whitespace

# Normalize path using os.path.normpath, which standardizes the path
normalizedPath = os.path.normpath(inputString)

# Clean up the path by replacing multiple leading slashes with a single slash
cleanedPath = re.sub(r'^/+', '/', normalizedPath)

# Output the result
print(cleanedPath)
