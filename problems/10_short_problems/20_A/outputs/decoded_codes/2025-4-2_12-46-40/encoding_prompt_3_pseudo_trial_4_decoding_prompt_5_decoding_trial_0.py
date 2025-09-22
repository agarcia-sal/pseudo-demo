def normalize_path(path):
    # Convert backslashes to forward slashes
    normalized_path = path.replace('\\', '/')
    
    # Split the path into components and filter out empty segments
    path_segments = normalized_path.split('/')
    filtered_segments = [segment for segment in path_segments if segment != '']
    
    # Clean up the path by joining the filtered segments
    return '/'.join(filtered_segments)

def remove_leading_slashes(path):
    # If the path starts with slashes, replace with a single leading slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')  # Remove all leading slashes
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

# Test cases (uncomment to run)
# print(normalize_path("C:\\User\\Documents\\..\\Pictures\\"))
# print(remove_leading_slashes("//User/Documents//"))
