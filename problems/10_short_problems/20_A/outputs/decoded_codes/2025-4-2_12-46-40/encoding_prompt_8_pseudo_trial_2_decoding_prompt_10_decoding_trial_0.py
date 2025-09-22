def normalize_path(input_path):
    """
    Normalize the input path by removing redundant separators and 
    unnecessary up-level references.
    """
    # Split the path into components and filter out empty elements
    components = input_path.split('/')
    normalized_components = [comp for comp in components if comp and comp != '.']

    # Join the components back into a normalized path
    normalized_input_path = '/'.join(normalized_components)
    
    return normalized_input_path


def replace_multiple_leading_slashes(path):
    """
    Ensure that the path starts with a single leading '/', 
    replacing any multiple leading slashes with a single one.
    """
    if path.startswith('/'):
        # Replace multiple leading slashes with a single '/'
        return '/' + path.lstrip('/')
    else:
        # Prepend a single slash if none exists
        return '/' + path


def main():
    # Step 1: Read the input file path from standard input
    user_input = input()

    # Step 2: Normalize the input path
    normalized_path = normalize_path(user_input)

    # Step 3: Ensure the normalized path starts with a single '/'
    final_path = replace_multiple_leading_slashes(normalized_path)

    # Step 4: Print the final normalized path
    print(final_path)


if __name__ == "__main__":
    main()
