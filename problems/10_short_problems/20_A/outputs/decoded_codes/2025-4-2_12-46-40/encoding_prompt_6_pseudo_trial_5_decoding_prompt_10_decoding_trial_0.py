import re

def main():
    # Read a string of file path data from standard input
    input_path = input()
    
    # Normalize the file path by removing any excessive slashes
    normalized_path = normalize_path(input_path)
    
    # Print the result to standard output
    print(normalized_path)

def normalize_path(path):
    """
    Normalizes the given file path by removing leading slashes.
    """
    cleaned_path = remove_leading_slashes(path)
    return cleaned_path

def remove_leading_slashes(path):
    """
    Removes leading slashes from the path using a regular expression.
    """
    modified_path = use_regular_expression_to_replace_leading_slashes(path)
    return modified_path

def use_regular_expression_to_replace_leading_slashes(path):
    """
    Replaces one or more leading slashes in the path with a single slash.
    """
    modified_path = re.sub(r'^/+', '/', path)  # Replace leading slashes with a single slash
    return modified_path

if __name__ == "__main__":
    main()
