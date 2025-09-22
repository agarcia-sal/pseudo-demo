import posixpath
import sys
import re

# Step 2: Read input path from user
inputPath = input().strip()

# Step 3: Normalize the input path
normalizedPath = posixpath.normpath(inputPath)

# Step 4: Adjust path to start with a single slash
adjustedPath = re.sub(r'^/+', '/', normalizedPath)

# Step 5: Output the final adjusted path
print(adjustedPath)
