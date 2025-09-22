def main():
    # Read the entire input from standard input (assumed to be a file path)
    raw_path = input()
    
    # Normalize the file path by removing redundant path separators
    normalized_path = normalize_path(raw_path)

    # Output the cleaned path
    print(normalized_path)

def normalize_path(path_string):
    """
    Normalize the file path by cleaning up redundant separators.
    """
    # Use built-in functionality to standardize the path
    cleaned_path = standardize(path_string)

    # Replace multiple leading slashes with a single slash at the start of the path
    cleaned_path = replace_leading_slashes(cleaned_path)
    
    return cleaned_path

def standardize(path_string):
    """
    Internal path normalization to clean up the path format.
    This is a placeholder for platform-specific normalization logic, 
    which could include converting backslashes to slashes etc.
    """
    # For simplicity, we will just return the path as is,
    # but in a robust implementation, this can be enhanced.
    return path_string.replace('\\', '/')  # Example: Converts backslashes to slashes

def replace_leading_slashes(cleaned_path):
    """
    Replace multiple leading slashes at the beginning of the path 
    with a single slash.
    """
    while cleaned_path.startswith('//'):
        cleaned_path = remove_one_slash_from_start(cleaned_path)
    
    return cleaned_path

def remove_one_slash_from_start(path):
    """
    Remove one leading slash from the given path.
    """
    return path[1:] if path else path

if __name__ == "__main__":
    main()
