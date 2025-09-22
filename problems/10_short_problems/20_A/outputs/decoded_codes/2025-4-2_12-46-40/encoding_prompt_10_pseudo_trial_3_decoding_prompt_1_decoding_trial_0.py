def normalize(path):
    # This function normalizes the file path
    # Replace this implementation with actual normalization logic
    return path  # Placeholder for normalization logic

def remove_leading_slashes(path):
    # This function returns the path with at most one leading slash
    if path.startswith('/'):
        # Remove leading slashes
        path = path.lstrip('/')
        if path:  # if path is not empty
            return '/' + path  # return a single leading slash + remaining part of path
        else:
            return ''  # return an empty string
    else:
        return path  # return the path as it is

# Main function logic
input_string = input()  # Read input from standard input

# Normalize the path by removing any redundant separators
normalized_path = normalize(input_string)

# Remove leading slashes from the normalized path, ensuring at most one leading slash remains
final_path = remove_leading_slashes(normalized_path)

# Output the final path
print(final_path)
