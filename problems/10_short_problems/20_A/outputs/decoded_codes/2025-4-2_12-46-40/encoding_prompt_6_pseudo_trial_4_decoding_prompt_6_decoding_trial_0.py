def normalize_path(input_path):
    # This function normalizes the given file path
    # For simplicity, here it replaces backslashes with forward slashes
    # and removes redundant slashes in the middle of the path.
    normalized_path = input_path.replace("\\", "/")  # Replace backslashes with forward slashes
    # Remove any redundant slashes (e.g., 'folder//subfolder' -> 'folder/subfolder')
    normalized_path = '/'.join(part for part in normalized_path.split('/') if part)
    return normalized_path

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Return with a single leading slash

def main():
    # Step 1: Read input from the standard input (user)
    user_input = input()  # Read file path input from the user

    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)

    # Step 3: Adjust leading slashes
    if normalized_path.startswith("/"):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)

    # Step 4: Output the final normalized path
    print(normalized_path)  # Display the normalized file path to the user

# Start the program
main()
