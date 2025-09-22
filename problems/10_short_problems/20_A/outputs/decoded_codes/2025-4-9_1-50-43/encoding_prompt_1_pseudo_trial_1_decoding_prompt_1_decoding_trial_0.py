# Step 1: Import Required Libraries
import os  # For path normalization
import re  # For regex operations (not strictly necessary in this case)

# Step 2: Read Input
inputPath = input().strip()  # Get user input and remove unnecessary whitespace

# Step 3: Normalize Path
normalizedPath = os.path.normpath(inputPath)  # Normalize the path

# Step 4: Adjust Path Format
finalPath = re.sub(r'^/{2,}', '/', normalizedPath)  # Replace leading slashes with a single slash

# Step 5: Print Result
print(finalPath)  # Output the final adjusted path
