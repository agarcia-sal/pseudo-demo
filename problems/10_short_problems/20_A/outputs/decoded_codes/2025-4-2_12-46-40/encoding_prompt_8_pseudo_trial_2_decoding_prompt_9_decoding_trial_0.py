def main():
    # Step 1: Read the input file path from standard input
    user_input = input()

    # Step 2: Normalize the input path
    normalized_path = normalize_path(user_input)

    # Step 3: Ensure the normalized path starts with a single '/'
    final_path = replace_multiple_leading_slashes(normalized_path)

    # Step 4: Print the final normalized path
    print(final_path)


def normalize_path(input_path):
    # Normalize the path by removing redundant components
    # Splitting the path by separators and filtering out unnecessary parts
    parts = input_path.split('/')
    normalized_parts = [part for part in parts if part and part != '.']
    return '/'.join(normalized_parts)


def replace_multiple_leading_slashes(path):
    # Check for slashes at the start of the path
    if path.startswith('/'):
        # Replace multiple leading slashes with a single '/'
        return '/' + path.lstrip('/')
    else:
        return '/' + path  # Prepend a single slash if none exists


# Run the main function
if __name__ == "__main__":
    main()
