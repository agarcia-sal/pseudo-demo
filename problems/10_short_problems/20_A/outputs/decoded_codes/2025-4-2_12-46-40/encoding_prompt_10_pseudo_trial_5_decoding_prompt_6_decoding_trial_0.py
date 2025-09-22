# Define the main procedure to normalize a path
def normalize_path():
    # Step 2: Read input from the user and store it in a variable
    input_path = input()  # Read input path

    # Step 3: Clean the input path
    # Normalize the input path by removing redundant slashes
    normalized_path = '/'.join(part for part in input_path.split('/') if part)  # Remove redundant slashes

    # Step 4: Substitute leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path  # If there's no leading slash, keep it as is

    # Step 5: Output the result
    print(final_path)  # Print the final normalized path

# Call the main procedure to execute the normalization
normalize_path()
