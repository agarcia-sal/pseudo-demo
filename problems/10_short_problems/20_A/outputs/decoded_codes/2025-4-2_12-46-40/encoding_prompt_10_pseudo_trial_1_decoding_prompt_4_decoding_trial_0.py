import os
import re

# Step 1: Define the variable to hold user input
input_string = input().strip()

# Step 2: Normalize the path using the os.path.normpath method
normalized_path = os.path.normpath(input_string)

# Step 3: Clean up the path to ensure a single leading slash
# Here we use regex to replace multiple leading slashes with a single one
cleaned_path = re.sub(r'^/+', '/', normalized_path)

# Step 4: Output the final cleaned path
print(cleaned_path)
