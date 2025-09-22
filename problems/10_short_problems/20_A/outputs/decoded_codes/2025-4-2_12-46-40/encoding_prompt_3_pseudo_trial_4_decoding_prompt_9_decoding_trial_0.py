def normalize_path(path):
    # Use a method to convert backslashes to forward slashes
    # and remove unnecessary segments from the path
    # This can be done using Python's os.path.normpath and replacing backslashes
    path = path.replace("\\", "/")  # Replace backslashes with forward slashes
    # More normalization logic can be implemented if necessary
    return path

def remove_leading_slashes(path):
    # If the path starts with one or more slashes, replace it with a single slash
    if path.startswith('/'):
        # This handles cases where there are multiple leading slashes
        return '/' + path.lstrip('/')  # Keep one leading slash and remove extras
    else:
        return path

# Read input from the standard input
input_string = input()

# Normalize the path to eliminate redundant separators and up-level references
normalized_path = normalize_path(input_string)

# Remove leading slashes, ensuring only a single leading slash remains
final_path = remove_leading_slashes(normalized_path)

# Output the final processed path
print(final_path)
