import os

# Start
# Step 2: Define Input
user_input = input()

# Step 3: Process Input
# Remove leading or trailing whitespace
normalized_path = user_input.strip()

# Normalize the file path
normalized_path = os.path.normpath(normalized_path)

# Step 4: Adjust Path Format
# Replace multiple leading slashes with a single one
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 5: Output Result
print(normalized_path)

# End
