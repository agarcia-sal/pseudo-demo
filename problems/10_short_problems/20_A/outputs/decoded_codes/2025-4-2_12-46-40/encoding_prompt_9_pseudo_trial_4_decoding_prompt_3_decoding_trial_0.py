def normalize_path(input_path):
    """
    Normalize the given file path by removing redundant sections.

    Args:
    input_path (str): The file path to normalize.

    Returns:
    str: The normalized file path.
    """
    # Split the path by '/' and filter out empty segments to remove redundant separators
    segments = [segment for segment in input_path.split('/') if segment]
    # Join the segments back together with a single '/' between them
    normalized = '/'.join(segments)
    return normalized


# Start of the program
if __name__ == "__main__":
    # Step 1: Read entire file path input
    file_path = input()

    # Step 2: Normalize the file path
    normalized_path = normalize_path(file_path)

    # Step 3: Ensure that the normalized path starts with a single forward slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 4: Output the final normalized path
    print(normalized_path)
