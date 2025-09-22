import re

def main():
    # Read input from standard input
    input_path = input()

    # Normalize the file path to remove redundant separators
    normalized_path = normalize_path(input_path)

    # Substitute leading slashes in the normalized path with a single slash
    final_path = substitute_leading_slashes(normalized_path)

    # Output the final processed path
    print(final_path)

def normalize_path(path: str) -> str:
    """
    Normalize the given path by ensuring that unnecessary segments are removed.
    This function can be expanded with more complex normalization logic if needed.
    For now, it will just handle basic cleanup.
    """
    # Replace multiple slashes with a single slash and remove current directory references
    normalized_path = re.sub(r'/+', '/', path)
    return normalized_path.strip()

def substitute_leading_slashes(path: str) -> str:
    """
    Replace multiple leading slashes in the path with a single slash.
    """
    return re.sub(r'^/+', '/', path)

if __name__ == "__main__":
    main()
