def normalize_path(raw_path):
    # Normalize the file path by standardizing the format and replacing leading slashes
    cleaned_path = standardize(raw_path)
    cleaned_path = replace_leading_slashes(cleaned_path)
    return cleaned_path

def standardize(path_string):
    # Placeholder for actual internal standardization logic
    # Currently, just returns the path string as is
    return path_string

def replace_leading_slashes(cleaned_path):
    # Replace multiple leading slashes with a single slash
    while cleaned_path.startswith('//'):
        cleaned_path = remove_one_slash_from_start(cleaned_path)
    return cleaned_path

def remove_one_slash_from_start(path):
    # Remove one leading slash from the given path
    return path[1:]  # Return the path without the first character

# Read the entire input from standard input (assumed to be a file path)
raw_path = input()

# Normalize the file path
normalized_path = normalize_path(raw_path)

# Output the cleaned path
print(normalized_path)
