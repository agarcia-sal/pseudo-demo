def normalize_file_path():
    # Step 1: Read the input
    input_path = input()  # Reading the file path from standard input

    # Step 2: Normalize the path
    normalized_path = input_path.replace("\\", "/")  # Replace backslashes with forward slashes for POSIX compliance

    # Step 3: Remove leading slashes
    if normalized_path.startswith('/'):
        # This will ensure that if there are multiple leading slashes, we keep only one
        final_path = '/' + normalized_path.lstrip('/')  # Strip leading slashes and prepend one
    else:
        final_path = normalized_path  # No leading slashes to remove

    # Step 4: Print the resulting path
    print(final_path)

# Main execution
normalize_file_path()
