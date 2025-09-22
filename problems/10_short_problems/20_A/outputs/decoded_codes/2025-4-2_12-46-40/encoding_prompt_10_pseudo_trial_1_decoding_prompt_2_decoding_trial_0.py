import os
import re

# Step 1: Define Variables
inputString = ""

# Step 2: Read Input
inputString = input().strip()

# Step 3: Normalize Path
normalizedPath = os.path.normpath(inputString)

# Step 4: Clean Up Path
cleanedPath = re.sub(r'^\/*', '/', normalizedPath)

# Step 5: Output Result
print(cleanedPath)
