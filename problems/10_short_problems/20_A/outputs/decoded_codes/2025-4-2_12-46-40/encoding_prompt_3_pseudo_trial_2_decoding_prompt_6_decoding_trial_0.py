# Function to normalize the path
def normalize_path(path_string):
    # Normalize the path using an appropriate method (placeholder for actual normalization logic)
    # In practice, this could be a more complex normalization depending on your requirements
    return path_string.replace("\\\\", "/").replace("\\", "/")  # Example normalization

# Function to remove leading slashes from the path
def remove_leading_slashes(path_string):
    # Return the path after removing excessive leading slashes with a single slash
    return '/' + path_string.lstrip('/')

# Read input from standard input
raw_path = input()  # Input path string

# Normalize the path
normalized_path = normalize_path(raw_path)

# Remove leading slashes from the normalized path
final_path = remove_leading_slashes(normalized_path)

# Print the resulting path
print(final_path)
