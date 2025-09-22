def normalize_path():
    # Step 2: Read Input
    input_path = input()

    # Step 3: Clean the Input Path
    normalized_path = '/'.join(part for part in input_path.split('/') if part)  # Remove redundant slashes

    # Step 4: Substitute Leading Slashes
    final_path = '/' + normalized_path if normalized_path else '/'  # Ensure it starts with a single slash

    # Step 5: Output the Result
    print(final_path)

# Step 1: Define Main Procedure entry point
normalize_path()
