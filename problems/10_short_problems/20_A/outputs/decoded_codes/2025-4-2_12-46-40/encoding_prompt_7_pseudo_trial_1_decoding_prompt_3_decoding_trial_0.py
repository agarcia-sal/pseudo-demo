def normalize_and_print_path():
    """
    Read a file path from standard input, normalize it by removing unnecessary components,
    and print the formatted path.
    """
    # Read input from the user and remove any leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace any occurrences of multiple leading slashes with a single slash
    final_path = normalize_leading_slashes(normalized_path)

    # Output the final formatted path
    print(final_path)

def normalize(input_path):
    """
    Normalize the file path by converting it to a standard format.
    This function resolves any '..' or '.' references in the path.
    """
    import os  # Import the os module for path manipulations

    # Use os.path.normpath to normalize the path
    return os.path.normpath(input_path)

def normalize_leading_slashes(path):
    """
    Replace any leading slashes in the path with a single slash.
    """
    # Split the path, ignore empty parts caused by leading slashes,
    # and join back with a single leading slash if the path is not empty.
    parts = path.split('/')
    cleaned_parts = [part for part in parts if part]  # Remove empty parts
    if cleaned_parts:
        return '/' + '/'.join(cleaned_parts)
    return '/'  # If there are no parts, return a single slash

# Example test run (uncomment the line below to run the function)
# normalize_and_print_path()
