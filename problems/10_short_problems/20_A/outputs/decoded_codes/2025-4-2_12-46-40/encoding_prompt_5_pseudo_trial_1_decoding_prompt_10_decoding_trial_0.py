def read_input():
    """Read input from the user and trim excess whitespace."""
    input_path = input().strip()
    return input_path

def normalize_path(path):
    """Normalize the file path by removing redundant separators and up-level references."""
    # Split the path by the separator and filter out empty segments
    path_segments = path.split('/')
    normalized_segments = []

    for segment in path_segments:
        if segment == '..':
            # Remove the last segment if '..' is encountered
            if normalized_segments:
                normalized_segments.pop()
        elif segment and segment != '.':
            # Only add non-empty segments and ignore current directory symbol
            normalized_segments.append(segment)

    # Join the normalized segments back into a path
    normalized_path = '/'.join(normalized_segments)
    return normalized_path

def ensure_single_leading_slash(path):
    """Ensure that the path starts with a single forward slash."""
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjusted_path = '/' + path.lstrip('/')
    else:
        # Path doesn't start with a slash, return it as is
        adjusted_path = path
    return adjusted_path

def main():
    """Main execution flow to read, normalize, and print the cleaned path."""
    user_input = read_input()
    normalized_input = normalize_path(user_input)
    final_path = ensure_single_leading_slash(normalized_input)
    print(final_path)

# Call the main function to execute the program
main()
