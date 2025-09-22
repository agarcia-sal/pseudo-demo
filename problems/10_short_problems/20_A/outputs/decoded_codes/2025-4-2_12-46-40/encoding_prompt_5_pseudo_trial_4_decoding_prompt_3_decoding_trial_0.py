def main():
    # Read the entire input from standard input (assumed to be a file path)
    raw_path = input()
    
    # Normalize the file path by removing redundant path separators
    normalized_path = normalize_path(raw_path)

    # Output the cleaned path
    print(normalized_path)

def normalize_path(path_string):
    """
    Normalize the input path by standardizing it and replacing
    multiple leading slashes with a single one.
    """
    # Standardize the path (could be platform-specific logic)
    cleaned_path = standardize(path_string)
    
    # Replace multiple leading slashes with a single slash
    cleaned_path = replace_leading_slashes(cleaned_path)
    
    return cleaned_path

def standardize(path_string):
    """
    This function would perform internal path normalization,
    such as converting backslashes to slashes (if needed).
    For now, it just returns the string as-is.
    """
    return path_string

def replace_leading_slashes(cleaned_path):
    """
    Replace multiple leading slashes in the cleaned path
    with a single leading slash.
    """
    while cleaned_path.startswith('//'):
        cleaned_path = remove_one_slash_from_start(cleaned_path)
    
    return cleaned_path

def remove_one_slash_from_start(path):
    """
    Remove one leading slash from the given path.
    """
    return path[1:]

# Entry point for the script
if __name__ == "__main__":
    main()
