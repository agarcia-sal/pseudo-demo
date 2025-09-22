import os

# Start of the program

# Step 2: Define Input
# Read a line of input from the user
input_path = input()

# Step 3: Process Input
# Remove any leading or trailing whitespace from the input
normalized_path = input_path.strip()

# Normalize the file path by resolving any relative components
# This will handle components like ".." or "."
normalized_path = os.path.normpath(normalized_path)

# Step 4: Adjust Path Format
# If the normalized path starts with one or more forward slashes, replace these with a single forward slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 5: Output Result
# Display the modified file path to the user
print(normalized_path)

# End of the program
