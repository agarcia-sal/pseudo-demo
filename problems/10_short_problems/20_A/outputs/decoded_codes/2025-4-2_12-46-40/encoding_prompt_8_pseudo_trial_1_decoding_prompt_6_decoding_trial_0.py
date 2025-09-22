import posixpath  # Import for handling file path operations
import sys  # Import for reading from system input
import re  # Import for regular expression operations

# Step 2: Read input path and strip extra whitespace
input_path = input().strip()

# Step 3: Normalize the path using the posixpath library
normalized_path = posixpath.normpath(input_path)

# Step 4: Ensure leading forward slash
# Replace any leading slashes with a single '/'
final_path = re.sub(r'^/+','/', normalized_path)

# Step 5: Output the final path
print(final_path)
