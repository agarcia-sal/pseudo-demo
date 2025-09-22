import re

# Function to normalize the path
def normalize_path(input_path):
    # Remove leading slashes from the path
    adjusted_path = remove_leading_slashes(input_path)
    # Return the normalized path
    return adjusted_path

# Function to remove leading slashes
def remove_leading_slashes(path):
    # Replace multiple leading slashes with a single slash
    return replace_multiple_leading_slashes_with_single_slash(path)

# Function to replace multiple leading slashes with a single slash
def replace_multiple_leading_slashes_with_single_slash(path):
    # Use a regular expression to perform the replacement
    return re.sub(r'^/+','/', path)

# Main program
if __name__ == "__main__":
    # Read input data from standard input (console)
    raw_file_path = input()

    # Normalize the path to a standard format
    normalized_path = normalize_path(raw_file_path)

    # Print the adjusted normalized path
    print(normalized_path)
