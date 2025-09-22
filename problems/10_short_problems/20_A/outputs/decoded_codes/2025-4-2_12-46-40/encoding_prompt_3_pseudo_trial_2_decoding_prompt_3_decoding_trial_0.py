def normalize_path(path_string):
    """
    Normalize the path by replacing multiple slashes with a single slash.
    """
    # Normalize path by using a single slash
    normalized = '/'.join(part for part in path_string.split('/') if part)
    return '/' + normalized if normalized else '/'

def remove_leading_slashes(path_string):
    """
    Remove all leading slashes from the string, retaining a single leading slash if the string is not empty.
    """
    stripped_path = path_string.lstrip('/')  # Remove leading slashes
    return '/' + stripped_path if stripped_path else ''

def main():
    # Read input from standard input
    raw_path = input()  # Getting the raw path string

    # Normalize the path
    normalized_path = normalize_path(raw_path)

    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)

    # Print the resulting path
    print(final_path)

if __name__ == '__main__':
    main()
