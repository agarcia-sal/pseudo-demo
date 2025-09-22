import os

def normalize_file_path():
    # Step 1: Read Input
    input_path = input().strip()  # Read the path and trim whitespace from ends

    # Step 2: Normalize Path
    normalized_path = os.path.normpath(input_path)  # Normalize the path using os.path.normpath

    # Step 3: Adjust Leading Slashes
    if normalized_path.startswith('/'):
        # If the path has multiple leading slashes, replace them with a single leading slash
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')

    # Step 4: Output Result
    print(final_path)  # Output the final normalized path

# Example of how to call the function:
# Uncomment the following line to use the function
# normalize_file_path()
