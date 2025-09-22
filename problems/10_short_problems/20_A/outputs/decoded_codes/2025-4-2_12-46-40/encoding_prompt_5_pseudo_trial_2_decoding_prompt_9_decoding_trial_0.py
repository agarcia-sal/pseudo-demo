import os

def normalize_file_path():
    # Step 1: Read the input
    input_path = input()  # Receive file path from standard input

    # Step 2: Normalize the path
    normalized_path = os.path.normpath(input_path).replace('\\', '/')  # Convert to POSIX format

    # Step 3: Remove leading slashes
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')

    # Step 4: Print the resulting path
    print(final_path)

# Main execution
normalize_file_path()
