def normalize_path(path_string):
    """
    Normalize the given path by replacing backslashes with forward slashes
    and removing any redundant slashes in the middle of the path.
    """
    # Replace backslashes with forward slashes and split into components
    components = path_string.replace("\\", "/").split("/")
    # Filter out empty components and join them back with a single slash
    normalized_components = [comp for comp in components if comp]
    return "/".join(normalized_components)


def remove_leading_slashes(path_string):
    """
    Remove leading slashes from the path. If the path starts with slashes,
    reduce them to a single leading slash.
    """
    if path_string.startswith("/"):
        # Strip leading slashes and return with a single leading slash
        return "/" + path_string.lstrip("/")
    return path_string


def main():
    # Read input from standard input
    raw_path = input()
    
    # Normalize the path
    normalized_path = normalize_path(raw_path)
    
    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)
    
    # Print the resulting path
    print(final_path)


if __name__ == "__main__":
    main()
