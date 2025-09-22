import posixpath
import sys
import re

# Step 2: Read input path
input_path = input().strip()

# Step 3: Normalize the path
normalized_path = posixpath.normpath(input_path)

# Step 4: Ensure leading forward slash
final_path = re.sub(r'^/+', '/', normalized_path)

# Step 5: Output the final path
print(final_path)
