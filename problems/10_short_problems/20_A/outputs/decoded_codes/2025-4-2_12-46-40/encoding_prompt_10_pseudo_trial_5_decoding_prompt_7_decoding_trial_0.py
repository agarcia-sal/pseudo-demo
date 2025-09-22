def normalize_path():
    # Step 2: Read Input
    input_path = input()
    
    # Step 3: Clean the Input Path
    # Normalize the input path by removing redundant slashes.
    # This is achieved by splitting the path by slashes and filtering out any empty parts,
    # then joining them back with a single slash.
    path_parts = input_path.split('/')
    cleaned_parts = [part for part in path_parts if part]  # Filter out empty strings
    normalized_path = '/'.join(cleaned_parts)  # Join parts with a single slash

    # Step 4: Substitute Leading Slashes
    # Ensure that the final path starts with a single leading slash,
    # if the normalized path is not empty.
    if normalized_path:
        final_path = '/' + normalized_path
    else:
        final_path = '/'  # If no valid parts, at least return a single slash

    # Step 5: Output the Result
    print(final_path)

# Call the main procedure to execute the path normalization
normalize_path()
