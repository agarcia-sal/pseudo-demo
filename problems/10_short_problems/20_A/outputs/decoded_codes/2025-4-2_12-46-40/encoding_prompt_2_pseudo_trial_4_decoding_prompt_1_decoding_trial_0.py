inputPath = input().strip()


import os
normalizedPath = os.path.normpath(inputPath)


import re
normalizedPath = re.sub(r'^/+','/', normalizedPath)


print(normalizedPath)


import os
import re

# Read Input
inputPath = input().strip()

# Normalize Path
normalizedPath = os.path.normpath(inputPath)

# Remove Leading Slashes
normalizedPath = re.sub(r'^/+','/', normalizedPath)

# Output Result
print(normalizedPath)
