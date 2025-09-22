def main():
    # Read a string of file path data from standard input
    input_path = input()

    # Normalize the file path by removing any excessive slashes
    normalized_path = normalize_path(input_path)

    # Print the result to standard output
    print(normalized_path)

def normalize_path(path):
    # Remove leading slashes from the path
    cleaned_path = remove_leading_slashes(path)
    return cleaned_path

def remove_leading_slashes(path):
    # Use regular expression to replace leading slashes with a single slash
    import re
    modified_path = use_regular_expression_to_replace_leading_slashes(path)
    return modified_path

def use_regular_expression_to_replace_leading_slashes(path):
    # Substitute the start of the string which matches one or more slashes with a single slash
    modified_path = re.sub(r'^/+','/', path)
    return modified_path

if __name__ == "__main__":
    main()
