import os
import re

# Step 1: Get Input
file_path = input().strip()

# Step 2: Normalize the Path
normalized_path = os.path.normpath(file_path)

# Step 3: Ensure Proper Format
if normalized_path.startswith('/'):
    normalized_path = re.sub(r'^/+', '/', normalized_path)  # Replace multiple leading slashes with a single slash
else:
    normalized_path = '/' + normalized_path  # Ensure it starts with a single slash

# Step 4: Display Result
print(normalized_path)
