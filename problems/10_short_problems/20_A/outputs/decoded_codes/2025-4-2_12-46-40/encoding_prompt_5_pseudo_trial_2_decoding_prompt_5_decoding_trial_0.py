def normalize_file_path():
    # Step 1: Read the input
    input_path = input()

    # Step 2: Normalize the path
    # Replace backslashes with forward slashes to convert to POSIX format
    normalized_path = input_path.replace('\\', '/')

    # Step 3: Remove leading slashes
    # Strip leading slashes to ensure a standardized format
    final_path = '/' + normalized_path.lstrip('/')

    # Step 4: Print the resulting path
    print(final_path)

# Main execution
normalize_file_path()
