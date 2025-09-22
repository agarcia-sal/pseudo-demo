import os
import re

# Step 1: Define Variables
inputString = input().strip()  # Read and strip leading/trailing whitespace

# Step 2: Normalize Path
normalizedPath = os.path.normpath(inputString)  # Normalize the path

# Step 3: Clean Up Path
cleanedPath = re.sub(r'^(?:/+)+', '/', normalizedPath)  # Replace multiple leading slashes with a single slash

# Step 4: Output Result
print(cleanedPath)
