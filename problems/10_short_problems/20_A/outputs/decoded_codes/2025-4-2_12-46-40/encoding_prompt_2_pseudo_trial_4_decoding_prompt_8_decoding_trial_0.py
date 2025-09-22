import os
import re

# Step 1: Read Input
inputPath = input().strip()

# Step 2: Normalize Path
normalizedPath = os.path.normpath(inputPath)

# Step 3: Remove Leading Slashes
normalizedPath = re.sub(r'^/+', '/', normalizedPath)

# Step 4: Output Result
print(normalizedPath)
