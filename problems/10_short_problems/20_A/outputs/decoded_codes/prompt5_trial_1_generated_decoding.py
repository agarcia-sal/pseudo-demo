import re

def read_input():
    # Read the entire input and trim any extra spaces from the beginning and end
    raw_path = input().strip()
    return raw_path

def normalize_path(input_path):
    # Normalize the file path by removing extra leading slashes
    normalized_path = remove_extra_leading_slashes_of(input_path)
    return normalized_path

def remove_extra_leading_slashes_of(path):
    # Use a regular expression to replace multiple leading slashes with a single leading slash
    cleaned_path = re.sub(r'^(/{2,})', '/', path)
    return cleaned_path

def output_normalized_path(normalized_path):
    # Output the normalized path to the user
    print(normalized_path)

# Main execution flow
input_path = read_input()
normalized_path = normalize_path(input_path)
output_normalized_path(normalized_path)
