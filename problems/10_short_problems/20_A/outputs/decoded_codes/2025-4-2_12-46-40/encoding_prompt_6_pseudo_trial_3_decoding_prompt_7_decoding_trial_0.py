def normalize_path(path):
    # Replace leading slashes with a single slash and normalize the path
    while path.startswith('/'):
        path = path[1:]
    return '/' + path

def main():
    # Read input from standard input and remove any leading/trailing whitespace
    input_string = input()
    trimmed_input_string = input_string.strip()  # Removes leading and trailing whitespace

    # Normalize the path, converting it to a standard format
    normalized_path = normalize_path(trimmed_input_string)

    # Output the final transformed path
    print(normalized_path)

# Call the main function only if this script is executed, not when imported
if __name__ == "__main__":
    main()
