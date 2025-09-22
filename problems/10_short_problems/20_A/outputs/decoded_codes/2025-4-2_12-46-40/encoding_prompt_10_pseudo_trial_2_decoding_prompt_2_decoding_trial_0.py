# Import Required Modules
import os          # For path handling
import sys         # For system operations
import re          # For regular expressions

# Read Input
input_string = input().strip()  # Read input from user and trim whitespace

# Normalize Path
normalized_path = os.path.normpath(input_string)  # Normalize the path

# Adjust Leading Slashes
# Replace one or more leading slashes with a single slash using regular expressions
adjusted_path = re.sub(r'^/+', '/', normalized_path)

# Output Result
print(adjusted_path)  # Print the final adjusted path
