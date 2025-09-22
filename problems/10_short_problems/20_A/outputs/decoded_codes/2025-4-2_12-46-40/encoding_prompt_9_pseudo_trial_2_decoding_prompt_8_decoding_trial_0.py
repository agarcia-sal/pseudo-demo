import os
import re

# Step 1: Get Input
file_path = input().strip()

# Step 2: Normalize the Path
normalized_path = os.path.normpath(file_path)

# Step 3: Ensure Proper Format
normalized_path = re.sub(r'^(\/+)', '/', normalized_path)

# Step 4: Display Result
print(normalized_path)
