import re

def main():
    # Read input data from standard input (console)
    raw_file_path = input()

    # Normalize the path to a standard format
    normalized_path = normalize_path(raw_file_path)

    # Print the adjusted normalized path
    print(normalized_path)

def normalize_path(input_path):
    # Remove leading slashes from the path
    adjusted_path = remove_leading_slashes(input_path)

    # Return the normalized path
    return adjusted_path

def remove_leading_slashes(path):
    # Replace multiple leading slashes with a single slash
    return replace_multiple_leading_slashes_with_single_slash(path)

def replace_multiple_leading_slashes_with_single_slash(path):
    # Use a regular expression to perform the replacement
    return re.sub(r'^/+','/', path)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
