import os

# Define a variable to store a normalized file path
normalized_path = ""

# Input Handling
user_input = input().strip()  # Read input and remove leading/trailing whitespace

# Normalize Path
normalized_path = os.path.normpath(user_input)  # Normalize the file path

# Remove Leading Slashes
normalized_path = normalized_path.lstrip('/')  # Remove leading slashes
if normalized_path:  # If the resulting path is not empty
    normalized_path = '/' + normalized_path  # Prepend a single slash

# Output Final Path
print(normalized_path)  # Display the transformed file path
