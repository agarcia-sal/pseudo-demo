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

    # Normalize the path to standard format (e.g., convert to POSIX path)
    normalized_path = normalize_format(trimmed_path)

    # Replace leading slash(es) with a single slash
    if normalized_path.startswith('/'):
        normalized_path = replace_leading_slashes_with_one(normalized_path)

    return normalized_path

def trim_whitespace(path):
    # Remove whitespace from the beginning and end of the string
    return path.strip()

def normalize_format(path):
    # Normalize path by replacing redundant elements (e.g., '..', '.')
    parts = []
    for part in path.split('/'):
        if part == '' or part == '.':
            # Ignore empty parts and current directory references
            continue
        elif part == '..':
            # If we encounter '..', we pop the last part unless we're at the root
            if parts:
                parts.pop()
        else:
            parts.append(part)
    # Join back to create a normalized path
    return '/' + '/'.join(parts)

def replace_leading_slashes_with_one(path):
    # Replace all leading slashes with a single slash
    return '/' + path.lstrip('/')

if __name__ == "__main__":
    main()
