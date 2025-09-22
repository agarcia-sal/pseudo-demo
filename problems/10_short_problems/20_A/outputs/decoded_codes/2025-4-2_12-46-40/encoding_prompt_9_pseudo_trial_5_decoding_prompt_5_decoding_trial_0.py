import os

def normalize_file_path():
    # Step 1: Read input from the user
    file_path = input()

    # Step 2: Normalize the file path
    # Resolve the file path to a canonical form using os.path.normpath
    normalized_path = os.path.normpath(file_path)

    # Step 3: Remove leading slashes
    # Checking if the normalized path starts with more than one slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]

    # Adding a single leading slash to the path
    final_path = '/' + normalized_path

    # Step 4: Output the final path
    print(final_path)

# Call the function to execute
normalize_file_path()
