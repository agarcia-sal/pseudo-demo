# Read a string from standard input for the file path
input_path = input().strip()  # Remove surrounding spaces

# Normalize the input path
normalized_path = input_path.replace('\\', '/')  # Convert backslashes to forward slashes

# Check for leading slashes and ensure only one is present
if normalized_path.startswith('/'):
    # Replace leading slashes with a single '/'
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]

# Prepend a single leading slash to the cleaned path
normalized_path = '/' + normalized_path

# Print the cleaned-up path
print(normalized_path)
