# Step 1: Read input from the user, stripping any leading or trailing whitespace
input_path = input().strip()

# Step 2: Normalize path - using Python's os.path.normpath to handle path normalization
import os
normalized_path = os.path.normpath(input_path)

# Step 3: Check and modify leading slashes
if normalized_path.startswith('/'):
    # Replace leading slashes with a single forward slash
    modified_path = '/' + normalized_path.lstrip('/')
else:
    modified_path = normalized_path  # No change if it doesn't start with a slash

# Step 4: Output the result
print(modified_path)
