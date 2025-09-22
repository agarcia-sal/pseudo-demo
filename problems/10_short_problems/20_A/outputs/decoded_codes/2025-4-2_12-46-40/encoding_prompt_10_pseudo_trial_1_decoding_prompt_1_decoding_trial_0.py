# Step 1: Define Variables
inputString = ""  # String variable to hold input from the user

# Step 2: Read Input
inputString = input().strip()  # Read input and remove leading and trailing whitespace

# Step 3: Normalize Path
# Assuming a normalization function exists. Replace with actual implementation if necessary.
import os
normalizedPath = os.path.normpath(inputString)  # Normalize the input string to a standard path format

# Step 4: Clean Up Path
import re
cleanedPath = re.sub(r'^/*', '/', normalizedPath)  # Replace multiple leading slashes with a single slash

# Step 5: Output Result
print(cleanedPath)  # Print the cleaned path
