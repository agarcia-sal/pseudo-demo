import os

# Step 1: Read Input 
inputPath = input().strip()  # Capture input and trim whitespace

# Step 2: Normalize File Path
normalizedPath = os.path.normpath(inputPath)  # Normalize the file path
if normalizedPath.startswith('/'):
    normalizedPath = '/' + normalizedPath.lstrip('/')  # Ensure it starts with a single slash
else:
    normalizedPath = '/' + normalizedPath  # Prepend a single slash if it doesn't start with one

# Step 3: Output Result
print(normalizedPath)  # Display the normalized path
