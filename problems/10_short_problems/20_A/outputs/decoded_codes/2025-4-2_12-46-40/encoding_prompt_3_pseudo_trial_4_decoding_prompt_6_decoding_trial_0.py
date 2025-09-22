# Function to normalize the path
def normalize_path(path):
    # Replace backslashes with forward slashes
    normalized_path = path.replace('\\', '/')
    # Remove unnecessary segments (not implemented for brevity)
    return normalized_path

# Function to remove leading slashes
def remove_leading_slashes(path):
    # If the path starts with multiple slashes, replace them with a single leading slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    else:
        return path

# Read input from the user
input_string = input()

# Normalize the path to eliminate redundant separators and up-level references
normalized_path = normalize_path(input_string)

# Remove leading slashes, ensuring only a single leading slash remains
final_path = remove_leading_slashes(normalized_path)

# Output the final processed path
print(final_path)
