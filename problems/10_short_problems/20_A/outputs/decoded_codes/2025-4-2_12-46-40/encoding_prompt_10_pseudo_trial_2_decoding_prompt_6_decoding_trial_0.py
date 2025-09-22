# Import necessary modules
import os  # for path handling
import re  # for regular expressions

# Read input from user and store it as a string, trimming whitespace
input_path = input().strip()

# Normalize the path to ensure correct format for the system
normalized_path = os.path.normpath(input_path)

# Adjust leading slashes - replace multiple leading slashes with a single slash
adjusted_path = re.sub(r'^/+','/', normalized_path)

# Output the final adjusted path
print(adjusted_path)
