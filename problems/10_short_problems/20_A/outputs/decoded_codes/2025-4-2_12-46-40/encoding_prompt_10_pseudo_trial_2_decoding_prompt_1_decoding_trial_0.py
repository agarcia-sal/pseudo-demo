# Import Required Modules
import os  # for path handling
import sys  # for system operations (not specifically used here but included as per pseudocode)
import re  # for regular expressions

# Read Input
user_input = input()  # Read input string from user

# Normalize Path
normalized_path = os.path.normpath(user_input)  # Normalize the path from input string

# Adjust Leading Slashes
adjusted_path = re.sub(r'^/+', '/', normalized_path)  # Replace leading slashes with a single slash

# Output Result
print(adjusted_path)  # Print the final adjusted path
