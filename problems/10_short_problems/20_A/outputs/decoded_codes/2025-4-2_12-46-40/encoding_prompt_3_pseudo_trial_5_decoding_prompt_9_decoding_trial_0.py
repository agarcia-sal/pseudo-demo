def read_input():
    # Read the entire input and remove leading/trailing spaces
    return input().strip()

def normalize_path(input_path):
    # Normalize the path by removing redundant separators and up-level references
    parts = input_path.split('/')
    normalized_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts or current directory references
        elif part == '..':
            if normalized_parts:
                normalized_parts.pop()  # Go up one directory level
        else:
            normalized_parts.append(part)
    
    # Join normalized parts into a single path
    return '/'.join(normalized_parts)

def format_path(normalized_path):
    # Replace any leading slashes with a single slash
    return normalized_path if not normalized_path.startswith('/') else normalized_path.lstrip('/')

def main():
    # Read input path
    input_path = read_input()
    
    # Normalize the path
    normalized_path = normalize_path(input_path)
    
    # Format the path
    formatted_path = format_path(normalized_path)

    # Output the final formatted path
    print(formatted_path)

if __name__ == "__main__":
    main()
