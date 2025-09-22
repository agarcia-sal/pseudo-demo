def normalize_path():
    # Step 2: Read Input
    input_path = input()
    
    # Step 3: Clean the Input Path
    # Normalize the path by removing redundant slashes
    normalized_path = '/'.join(part for part in input_path.split('/') if part)

    # Step 4: Substitute Leading Slashes
    # Ensure a single leading slash if the normalized path is not empty
    final_path = '/' + normalized_path if normalized_path else ''

    # Step 5: Output the Result
    print(final_path)

# Call the main procedure
normalize_path()
