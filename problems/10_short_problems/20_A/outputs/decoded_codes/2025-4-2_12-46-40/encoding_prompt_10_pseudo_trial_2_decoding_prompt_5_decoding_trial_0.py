import os  # Import module for path handling
import sys  # Import module for system operations
import re  # Import module for regular expressions

# Read input from user
input_path = input().strip()  # Trim any leading or trailing whitespace

# Normalize the path using os module to ensure it uses the correct format for the system
normalized_path = os.path.normpath(input_path)

# Adjust leading slashes: Replace multiple leading slashes with a single slash using regular expressions
adjusted_path = re.sub(r'^/+','/', normalized_path)

# Output the final adjusted path
print(adjusted_path)
