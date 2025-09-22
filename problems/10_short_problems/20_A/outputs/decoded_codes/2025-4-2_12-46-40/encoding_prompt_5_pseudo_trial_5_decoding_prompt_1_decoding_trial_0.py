def normalize_file_path():
    # STEP 1: Read the file path from standard input
    file_path = input().strip()  # Remove any extra spaces

    # STEP 2: Normalize the file path
    import os  # using os.path to handle path normalization
    normalized_path = os.path.normpath(file_path)

    # STEP 3: Remove leading slashes
    final_path = normalized_path.lstrip('/')  # Remove all leading slashes
    final_path = '/' + final_path  # Add a single leading slash back

    # STEP 4: Output the result
    print(final_path)

# To call the function, you would use:
# normalize_file_path()
