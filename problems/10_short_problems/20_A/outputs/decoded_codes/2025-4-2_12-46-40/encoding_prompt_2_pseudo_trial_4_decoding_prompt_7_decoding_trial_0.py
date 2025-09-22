import re  # Importing the regular expression module for pattern matching

# Step 1: Read Input
inputPath = input().strip()  # Getting user input and removing leading/trailing whitespace

# Step 2: Normalize Path
# Since we need to normalize the path, we will replace any occurrences of double slashes
# with a single slash, and also handle case sensitivity or other normalizations as needed.
normalizedPath = re.sub(r'//+', '/', inputPath)  # Replace multiple slashes with a single slash

# Step 3: Remove Leading Slashes
# This step will use a regular expression to replace any leading slashes with a single slash
normalizedPath = re.sub(r'^/+','/', normalizedPath)  # Replace leading slashes with a single slash

# Step 4: Output Result
print(normalizedPath)  # Display the modified path
