import os

# Read the input from the user and strip extra spaces
input_path = input().strip()

# Normalize the file path using standard path normalization rules
normalized_path = os.path.normpath(input_path)

# Replace any occurrence of multiple leading slashes with a single leading slash
if normalized_path.startswith('/'):
    # If path starts with a slash, just keep the first one and remove others
    output_path = '/' + normalized_path.lstrip('/')
else:
    # If not, just use the normalized path without leading slashes
    output_path = normalized_path.lstrip('/')

# Print the final adjusted path
print(output_path)
