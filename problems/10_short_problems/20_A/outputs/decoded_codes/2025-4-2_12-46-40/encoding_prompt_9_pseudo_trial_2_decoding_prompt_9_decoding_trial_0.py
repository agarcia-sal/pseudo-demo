import os  # Import os for handling file paths
import re  # Import re for regular expressions

# Step 1: Get Input
raw_path = input().strip()  # Read file path and remove surrounding whitespace

# Step 2: Normalize the Path
normalized_path = os.path.normpath(raw_path)  # Normalize the path

# Step 3: Ensure Proper Format
# Replace multiple leading slashes with a single one
if normalized_path.startswith('/'):
    # Collapse multiple leading slashes to a single slash
    normalized_path = re.sub(r'^/+','/', normalized_path)
else:
    normalized_path = '/' + normalized_path  # If it doesn't start with '/', add one

# Step 4: Display Result
print(normalized_path)  # Output the final normalized path
