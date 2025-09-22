import posixpath
import sys
import re

# Step 2: Read input path
input_path = input().strip()  # Read input and strip whitespace

# Step 3: Normalize the path
normalized_path = posixpath.normpath(input_path)  # Normalize the path using posixpath

# Step 4: Ensure leading forward slash
final_path = re.sub(r'^/+','/', normalized_path)  # Replace any leading slashes with a single '/'

# Step 5: Output the final path
print(final_path)  # Output the normalized path
