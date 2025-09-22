def normalize_path():
    # Step 1: Read input from standard input and remove leading/trailing whitespace
    raw_path = input().strip()

    # Step 2: Normalize the path to handle any redundant separators
    # Replace multiple leading slashes with a single slash
    if raw_path.startswith('/'):
        normalized_path = '/' + '/'.join(part for part in raw_path.split('/') if part)
    else:
        normalized_path = '/'.join(part for part in raw_path.split('/') if part)

    # Step 3: Output the normalized path
    print(normalized_path)

# Call the function to execute the normalization process
normalize_path()
