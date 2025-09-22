def main():
    # Read input from standard input
    raw_file_path = input()
    
    # Normalize the file path by removing trailing slashes and redundant elements
    normalized_file_path = normalize_path(raw_file_path)

    # Print the resulting normalized file path
    print(normalized_file_path)

def normalize_path(input_path: str) -> str:
    # Remove surrounding whitespace from the input path
    trimmed_path = trim_whitespace(input_path)

    # Normalize the path to standard format (similar to POSIX path)
    normalized_path = normalize_format(trimmed_path)

    # Replace leading slash(es) with a single slash
    if normalized_path.startswith('/'):
        normalized_path = replace_leading_slashes_with_one(normalized_path)

    return normalized_path

def trim_whitespace(path: str) -> str:
    # Remove whitespace from the beginning and end of the string
    return path.strip()

def normalize_format(path: str) -> str:
    # Simplify the path by removing redundant components
    parts = path.split('/')
    simplified_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts and current directory indicators
        elif part == '..':
            if simplified_parts:
                simplified_parts.pop()  # Remove last valid directory
        else:
            simplified_parts.append(part)
    
    # Join the normalized parts and return
    return '/' + '/'.join(simplified_parts)

def replace_leading_slashes_with_one(path: str) -> str:
    # Replace all leading slashes with a single slash
    return '/' + path.lstrip('/')

# Entry point of the program
if __name__ == "__main__":
    main()
