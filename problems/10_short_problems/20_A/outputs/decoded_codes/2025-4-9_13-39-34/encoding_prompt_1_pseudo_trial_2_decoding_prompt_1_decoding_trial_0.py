# Step 1: Read the user input
userInput = input().strip()  # Read input and remove leading and trailing whitespace

# Step 2: Normalize the path
normalizedPath = userInput.replace('\\', '/')  # Normalizing by replacing backslashes with slashes (basic normalization)

# Step 3: Remove extra leading slashes
if normalizedPath.startswith('/'):  # Check if the normalized path starts with slashes
    # Replace multiple leading slashes with a single slash
    normalizedPath = '/' + normalizedPath.lstrip('/')  # Keep one leading slash and remove others

# Step 4: Output the final result
print(normalizedPath)
