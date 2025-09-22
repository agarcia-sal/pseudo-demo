import re

# Function to normalize the file path
def normalize_path(input_path):
    # Remove leading slashes from the path
    adjusted_path = remove_leading_slashes(input_path)
    return adjusted_path

# Function to remove multiple leading slashes
def remove_leading_slashes(path):
    # Replace multiple leading slashes with a single slash using a regular expression
    return re.sub(r'^/+','/', path)

# Main program execution
# Read input data from standard input (console)
raw_file_path = input()

# Normalize the path to a standard format
normalized_path = normalize_path(raw_file_path)

# Print the adjusted normalized path
print(normalized_path)
