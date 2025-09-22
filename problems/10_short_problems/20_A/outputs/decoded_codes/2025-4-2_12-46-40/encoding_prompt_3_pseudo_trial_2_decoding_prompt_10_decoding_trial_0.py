def normalize_path(path_string):
    """
    Normalize the path by replacing backslashes with forward slashes
    and removing any redundant slashes.
    """
    # Replace backslashes with forward slashes for cross-platform compatibility
    normalized = path_string.replace("\\", "/")
    
    # Remove any redundant slashes within the path
    normalized = "/".join(part for part in normalized.split("/") if part)
    
    return normalized

def remove_leading_slashes(path_string):
    """
    Remove all leading slashes, leaving only a single slash if the path is not empty.
    """
    # Remove leading slashes and ensure one leading slash is present if the path is not empty
    return "/" + path_string.lstrip("/")

def main():
    # Read input from standard input
    raw_path = input()
    
    # Normalize the path
    normalized_path = normalize_path(raw_path)
    
    # Remove leading slashes from the normalized path
    final_path = remove_leading_slashes(normalized_path)
    
    # Print the resulting path
    print(final_path)

if __name__ == "__main__":
    main()
