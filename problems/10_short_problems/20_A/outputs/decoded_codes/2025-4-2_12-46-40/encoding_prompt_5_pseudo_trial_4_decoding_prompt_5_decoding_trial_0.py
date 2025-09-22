def main():
    # Read the entire input from standard input (assumed to be a file path)
    raw_path = input()
    
    # Normalize the file path by removing redundant path separators
    normalized_path = normalize_path(raw_path)

    # Output the cleaned path
    print(normalized_path)

def normalize_path(path_string):
    # Use the built-in functionality to normalize the path
    cleaned_path = standardize(path_string)

    # Replace multiple leading slashes with a single slash at the start of the path
    cleaned_path = replace_leading_slashes(cleaned_path)
    
    return cleaned_path

def standardize(path_string):
    # This function simulates internal path normalization
    # Here, we assume the shaping of the path based on standard requirements
    return path_string  # Placeholder for actual internal standardization logic

def replace_leading_slashes(cleaned_path):
    # Check if the path starts with one or more slashes
    while cleaned_path.startswith('//'):
        cleaned_path = remove_one_slash_from_start(cleaned_path)
    
    return cleaned_path

def remove_one_slash_from_start(path):
    # Remove one leading slash from the given path
    return path[1:]

# The entry point for the script
if __name__ == "__main__":
    main()
