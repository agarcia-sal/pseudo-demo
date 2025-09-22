import os
import re

# Step 1: Read Input
inputPath = input().strip()

# Step 2: Normalize Path
# Using os.path.normpath to normalize the provided path
normalizedPath = os.path.normpath(inputPath)

# Step 3: Remove Leading Slashes
# Replace any leading slashes with a single slash using regex
normalizedPath = re.sub(r'^/+', '/', normalizedPath)

# Step 4: Output Result
print(normalizedPath)
