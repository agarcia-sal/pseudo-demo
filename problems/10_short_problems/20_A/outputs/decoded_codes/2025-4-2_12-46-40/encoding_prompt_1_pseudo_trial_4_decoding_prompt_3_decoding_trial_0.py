def normalize_file_path():
    # Step 1: Read input and trim whitespace
    input_path = input().strip()

    # Step 2: Normalize the file path
    # Split the path by '/' and filter out empty components
    path_components = [component for component in input_path.split('/') if component]
    # Join the components with a single '/' and add the leading '/'
    normalized_path = '/' + '/'.join(path_components)

    # Step 3: Output the normalized path
    print(normalized_path)

# The function can be called to perform path normalization
normalize_file_path()
