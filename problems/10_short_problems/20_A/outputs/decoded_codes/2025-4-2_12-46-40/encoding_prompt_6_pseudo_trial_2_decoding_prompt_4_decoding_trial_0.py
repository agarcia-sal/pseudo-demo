def normalize_path(input_path):
    # This function transforms the file path to a standard format
    # In this example, we'll replace backslashes with forward slashes for consistency
    normalized_path = input_path.replace("\\", "/")
    return normalized_path

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Return the path with a single leading slash

# Begin the program
input_path = input().strip()  # Read input from standard input and remove extra spaces
normalized_path = normalize_path(input_path)  # Normalize the path
final_path = replace_leading_slashes(normalized_path)  # Replace leading slashes
print(final_path)  # Output the final normalized path
