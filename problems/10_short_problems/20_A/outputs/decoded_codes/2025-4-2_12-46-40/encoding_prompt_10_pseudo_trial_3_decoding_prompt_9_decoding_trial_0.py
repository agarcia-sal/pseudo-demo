def normalize(path):
    # This function normalizes the file path
    # For now, we assume that this just returns the path cleaned of extraneous separators
    # In real implementation, you would include logic here to handle normalization
    return path.replace("//", "/")  # Example normalization logic

def remove_leading_slashes(path):
    # This function returns the path with at most one leading slash
    if path.startswith('/'):
        path = path.lstrip('/')  # Remove leading slashes
        if path:  # If there's still something left
            return '/' + path  # Add a single leading slash
        else:
            return ''  # Return an empty string if nothing is left
    else:
        return path  # Return path as is if it doesn't start with a slash

# Main logic
input_string = input()  # Read input from standard input
normalized_path = normalize(input_string)  # Normalize the input string
final_path = remove_leading_slashes(normalized_path)  # Remove leading slashes
print(final_path)  # Output the final path
