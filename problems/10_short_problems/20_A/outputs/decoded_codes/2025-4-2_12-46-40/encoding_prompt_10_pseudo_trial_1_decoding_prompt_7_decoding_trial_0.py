import re
import os

# Step 1: Define Variables
inputString = ""

# Step 2: Read Input
inputString = input().strip()  # Read input and remove leading/trailing whitespace

# Step 3: Normalize Path
normalizedPath = os.path.normpath(inputString)  # Normalize the input path using os.path.normpath

# Step 4: Clean Up Path
# Replace multiple leading slashes with a single slash
cleanedPath = re.sub(r'^/+', '/', normalizedPath)

# Step 5: Output Result
print(cleanedPath)  # Print the cleaned path
