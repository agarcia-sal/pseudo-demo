def normalize_and_print_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace any leading slashes with a single slash
    final_path = normalized_path.lstrip('/')

    # Output the final formatted path
    print(final_path)

def normalize(input_path):
    # Normalize the file path by converting it to a standard format
    # This involves resolving any '..' or '.' references in the path
    import os
    return os.path.normpath(input_path)

# Note: You may test the function with various paths and edge cases such as:
# normalize_and_print_path()  # Example input: "//home//user/../documents/"
