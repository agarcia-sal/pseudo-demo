def main():
    # Read input from standard input
    raw_path = input()  # This will receive the raw path string

    # Normalize the path
    normalized_path = normalize_path(raw_path)

    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)

    # Print the resulting path
    print(final_path)


def normalize_path(path_string):
    """ Normalize the path by replacing backslashes with forward slashes. """
    # Normalize the path by using forward slashes for consistency
    normalized_path = path_string.replace('\\', '/')
    return normalized_path


def remove_leading_slashes(path_string):
    """ Remove any leading slashes from the start of the string. """
    # Remove leading slashes, ensuring only one at the start if any
    return '/' + path_string.lstrip('/')


# Entry point for the program execution
if __name__ == "__main__":
    main()
