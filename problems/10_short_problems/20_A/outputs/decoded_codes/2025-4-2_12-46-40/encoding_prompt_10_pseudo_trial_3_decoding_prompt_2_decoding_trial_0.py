def normalize(path):
    # This function normalizes the file path
    # Replace this with the actual normalization logic
    return path  # Example placeholder logic

def remove_leading_slashes(path):
    # This function returns the path with at most one leading slash
    if path.startswith('/'):
        # Remove all leading slashes
        path = path.lstrip('/')
        if path:  # Check if the path is not empty
            return '/' + path  # Return a single leading slash with the remaining part
        else:
            return ''  # Return an empty string if the path was empty after removing slashes
    else:
        return path  # Return the path as is if it doesn't start with a slash

# Main part of the code
input_string = input()  # Read input from standard input
normalized_path = normalize(input_string)  # Normalize the input string
final_path = remove_leading_slashes(normalized_path)  # Remove leading slashes from the normalized path
print(final_path)  # Output the final path
