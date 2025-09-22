def main():
    # Read input from standard input
    input_string = input()
    
    # Normalize the path to ensure a consistent format
    normalized_path = normalize_path(input_string)
    
    # Remove leading slashes to ensure a single leading slash (if present)
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final computed path
    print(final_path)


def normalize_path(input_string):
    """
    Normalize the input string to a standard file path format.
    This function transforms the input path according to POSIX rules.
    """
    # Split the path into components, remove empty components, and join them back
    components = input_string.split("/")
    normalized_components = [component for component in components if component]
    
    # Join components back into a normalized path
    normalized_path = "/".join(normalized_components)
    
    # Return the normalized path
    return normalized_path


def remove_leading_slashes(path):
    """
    Remove leading slashes in the path, ensuring the result has at most one leading slash.
    """
    if path.startswith("/"):
        # Remove all leading slashes and ensure there's one leading slash
        return "/" + path.lstrip("/")
    return path


if __name__ == "__main__":
    main()
