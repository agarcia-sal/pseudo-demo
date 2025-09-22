def normalize_file_path():
    # Step 1: Read input and trim whitespace
    input_path = input().strip()

    # Step 2: Normalize the file path
    # Split the input path by slashes and filter out empty segments
    path_segments = filter(None, input_path.split('/'))
    normalized_path = '/' + '/'.join(path_segments)

    # Step 3: Output the normalized path
    print(normalized_path)

# Execute the function to normalize the file path
normalize_file_path()
