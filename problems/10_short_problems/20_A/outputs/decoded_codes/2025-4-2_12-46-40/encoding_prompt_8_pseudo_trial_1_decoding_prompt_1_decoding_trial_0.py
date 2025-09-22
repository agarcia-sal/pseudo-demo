# Step 1: Initialize environment
import posixpath
import sys
import re

# Step 2: Read input path
inputPath = input().strip()

# Step 3: Normalize the path
normalizedPath = posixpath.normpath(inputPath)

# Step 4: Ensure leading forward slash
finalPath = re.sub(r'^/+','/', normalizedPath)

# Step 5: Output the final path
print(finalPath)
