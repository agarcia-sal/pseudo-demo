def main():
    # Read input from standard input
    raw_file_path = input()

    # Normalize the file path by removing trailing slashes and redundant elements
    normalized_file_path = normalize_path(raw_file_path)

    # Print the resulting normalized file path
    print(normalized_file_path)

def normalize_path(input_path):
    # Remove surrounding whitespace from the input path
    trimmed_path = trim_whitespace(input_path)

    # Normalize the path to standard format
    normalized_path = normalize_format(trimmed_path)

    # Replace leading slash(es) with a single slash
    if normalized_path.startswith('/'):
        normalized_path = replace_leading_slashes_with_one(normalized_path)

    return normalized_path

def trim_whitespace(path):
    # Remove whitespace from the beginning and end of the string
    return path.strip()

def normalize_format(path):
    # Split the path into components and filter out empty elements
    components = path.split('/')
    simplified_components = []
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            # Remove last added component if possible
            if simplified_components:
                simplified_components.pop()
        else:
            simplified_components.append(component)
    
    # Join the components back into a normalized path
    normalized_path = '/'.join(simplified_components)

    # Ensure the normalized path does not end with a slash (unless it's the root)
    if not normalized_path and path.startswith('/'):
        return '/'
    
    return normalized_path

def replace_leading_slashes_with_one(path):
    # Replace all leading slashes with a single slash
    return '/' + path.lstrip('/')

# Entry point of the program
if __name__ == "__main__":
    main()
