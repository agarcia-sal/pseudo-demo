import os

# Function to normalize the file path using os.path.normpath
def normalize(path):
    # Normalize the path by removing any redundant separators
    return os.path.normpath(path)

# Function to remove leading slashes from the path
def remove_leading_slashes(path):
    # If the path starts with a slash, we will process it
    if path.startswith('/'):
        # Remove leading slashes
        path = path.lstrip('/')
        # If the remaining path is not empty, prepend a single leading slash
        if path:
            return '/' + path
        else:
            return ''  # Return an empty string if nothing remains
    else:
        return path  # Return the path as is if it doesn't start with a slash

# Main program execution
input_string = input()  # Read input from standard input
normalized_path = normalize(input_string)  # Normalize the input path
final_path = remove_leading_slashes(normalized_path)  # Remove leading slashes

# Output the final path
print(final_path)  # Print the cleaned-up path
