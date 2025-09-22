def normalize_file_path():
    # Read input from standard input
    input_path = input().strip()

    # Normalize the file path
    normalized_path = remove_unnecessary_separators(input_path)

    # Ensure the path starts with a single slash
    if normalized_path.startswith('//'):
        normalized_path = normalized_path.replace('//', '/', 1)  # Only replace the first occurrence

    # Output the final normalized path
    print(normalized_path)

def remove_unnecessary_separators(path):
    # Replace multiple consecutive slashes with a single slash
    # Strip leading and trailing slashes from the path
    # We will use 're.sub' for this purpose
    import re
    # Replace multiple slashes with a single slash and trim the path
    return re.sub(r'/+', '/', path).strip('/')

# Call the function to execute
normalize_file_path()
