import os

def normalize_path():
    # Step 1: Read input from standard input
    input_string = input()

    # Step 2: Normalize the input path string
    # This operation cleans up the path, ensuring proper formatting
    normalized_path = os.path.normpath(input_string)

    # Step 3: Remove leading slashes
    # Ensure that there's at most one leading slash in the final output
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')

    # Step 4: Output the final normalized path
    print(final_path)

# Call the function to execute the path normalization
normalize_path()
