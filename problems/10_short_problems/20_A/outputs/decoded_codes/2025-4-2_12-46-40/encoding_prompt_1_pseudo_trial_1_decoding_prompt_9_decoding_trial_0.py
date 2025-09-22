import os

# Function to normalize the file path
def normalize_file_path(file_path):
    # Remove leading and trailing whitespace
    trimmed_path = file_path.strip()
    
    # Normalize the file path by removing redundant separators and up-level references
    normalized_path = os.path.normpath(trimmed_path)

    # Adjust leading slashes to ensure only one leading slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]  # Remove the leading slash
    adjusted_path = '/' + normalized_path  # Add a single leading slash

    return adjusted_path

# Start of program
# Read input: Get file path from standard input
input_path = input()

# Normalize the file path using the defined function
result = normalize_file_path(input_path)

# Output the result
print(result)
