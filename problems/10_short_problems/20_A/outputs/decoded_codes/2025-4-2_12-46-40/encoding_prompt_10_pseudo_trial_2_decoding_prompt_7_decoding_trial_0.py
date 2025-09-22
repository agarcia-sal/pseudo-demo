# Importing the required modules
import os  # Module for path handling
import sys  # Module for system operations, not necessarily used here
import re  # Module for regular expressions

# Step 1: Read input from the user and store it as a string
input_path = input().strip()  # Read input and trim whitespace

# Step 2: Normalize the path to ensure it uses the correct format for the system
normalized_path = os.path.normpath(input_path)  # Normalize the path using os

# Step 3: Adjust leading slashes
# Use regex to replace one or more leading slashes with a single slash
adjusted_path = re.sub(r'^/+','/', normalized_path)  # Replace leading slashes

# Step 4: Output the final adjusted path
print(adjusted_path)  # Print the adjusted path
