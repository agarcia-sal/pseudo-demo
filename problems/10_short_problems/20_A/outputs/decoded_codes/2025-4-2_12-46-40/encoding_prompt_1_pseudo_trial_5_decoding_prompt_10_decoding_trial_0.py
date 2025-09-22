def main():
    # Read input from standard input
    raw_file_path = input()
    
    # Normalize the file path by removing trailing slashes and redundant elements
    normalized_file_path = normalize_path(raw_file_path)
    
    # Print the resulting normalized file path
    print(normalized_file_path)

def normalize_path(input_path: str) -> str:
    """
    Normalize the input file path by trimming whitespace, normalizing format,
    and ensuring a single leading slash if it exists.
    """
    trimmed_path = trim_whitespace(input_path)
    
    normalized_path = normalize_format(trimmed_path)
    
    # Replace leading slashes with a single slash
    if normalized_path.startswith('/'):
        normalized_path = replace_leading_slashes_with_one(normalized_path)
    
    return normalized_path

def trim_whitespace(path: str) -> str:
    """
    Remove leading and trailing whitespace from the path.
    """
    return path.strip()

def normalize_format(path: str) -> str:
    """
    Simplify the path by replacing redundant path components.
    This could include resolving '.' and '..' segments,
    Removing extra slashes, etc.
    """
    # Splitting path into components to process individually
    components = path.split('/')
    simplified_path = []

    for segment in components:
        if segment == '' or segment == '.':
            continue
        elif segment == '..':
            if simplified_path:
                simplified_path.pop()  # Go back one directory if possible
        else:
            simplified_path.append(segment)
    
    return '/' + '/'.join(simplified_path)

def replace_leading_slashes_with_one(path: str) -> str:
    """
    Replace all leading slashes in the path with a single slash.
    """
    return '/' + path.lstrip('/')

if __name__ == "__main__":
    main()
