# Step 1: Read Input
input_path = input().strip()  # Accepts input and removes leading/trailing whitespace

# Step 2: Normalize Path
import os
normalized_path = os.path.normpath(input_path)  # Normalizes the path using correct separators

# Step 3: Modify Leading Slashes
if normalized_path.startswith('/'):  # Check for leading forward slashes
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace with a single leading slash

# Step 4: Output Result
print(normalized_path)  # Display the modified path
