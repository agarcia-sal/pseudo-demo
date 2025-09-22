import os

# Start the program

# Read a line of input from the user
input_path = input()

# Process Input
# Remove leading or trailing whitespace
trimmed_path = input_path.strip()

# Normalize the file path
normalized_path = os.path.normpath(trimmed_path)

# Adjust Path Format
# If the normalized path starts with one or more slashes,
# replace these with a single forward slash
if normalized_path.startswith('/'):
    adjusted_path = '/' + normalized_path.lstrip('/')
else:
    adjusted_path = normalized_path

# Output Result
# Display the modified file path to the user
print(adjusted_path)

# End the program
