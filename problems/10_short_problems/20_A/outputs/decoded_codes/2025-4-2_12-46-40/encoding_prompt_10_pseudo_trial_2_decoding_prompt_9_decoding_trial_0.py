import os  # Import module for path handling
import re  # Import module for regular expressions

# Read input from user and trim whitespace
input_path = input().strip()

# Normalize the path to ensure it uses the correct format for the system
normalized_path = os.path.normpath(input_path)

# Use a regular expression to replace leading slashes with a single slash
adjusted_path = re.sub(r'^/+', '/', normalized_path)

# Print the final adjusted path
print(adjusted_path)
