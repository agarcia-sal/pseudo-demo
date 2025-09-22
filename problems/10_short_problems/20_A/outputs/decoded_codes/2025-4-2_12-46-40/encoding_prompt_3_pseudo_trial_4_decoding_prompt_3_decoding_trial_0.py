def main():
    # Read input from the standard input
    input_string = input()
    
    # Normalize the path to eliminate redundant separators and up-level references
    normalized_path = normalize_path(input_string)
    
    # Remove leading slashes, ensuring only a single leading slash remains
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final processed path
    print(final_path)

def normalize_path(path):
    # Normalize the path by replacing backslashes with forward slashes and removing unnecessary segments
    # Split the path into parts, filtering out empty segments and '.' segments
    parts = path.replace('\\', '/').split('/')
    normalized_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts and current directory references
        elif part == '..':
            if normalized_parts:
                normalized_parts.pop()  # Go up one level in the path if possible
        else:
            normalized_parts.append(part)  # Add the valid part to the normalized path

    # Join the parts back together, ensuring there are no redundant slashes
    return '/' + '/'.join(normalized_parts)

def remove_leading_slashes(path):
    # If the path starts with one or more slashes, replace it with a single slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    return path

# Execute main function
if __name__ == "__main__":
    main()
