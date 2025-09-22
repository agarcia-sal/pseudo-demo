def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = normalizer(input_path)
    
    # Replace any leading slashes with a single slash
    formatted_path = replace_leading_slashes(normalized_path)
    
    # Output the formatted path
    print(formatted_path)

def normalizer(path):
    # Replace multiple slashes with a single one
    return '/'.join(filter(None, path.split('/')))

def replace_leading_slashes(path):
    # Replace leading slashes with a single slash
    while path.startswith('/'):
        path = path[1:]
    return '/' + path if path else ''

# You can call the function here or use it in the main execution block
normalize_and_format_path()
