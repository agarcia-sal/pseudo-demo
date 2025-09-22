def main():
    # Read input from the standard input
    input_string = input()
    
    # Normalize the path to eliminate redundant separators and up-level references
    normalized_path = normalize_path(input_string)
    
    # Remove leading slashes, ensuring only a single leading slash remains
    final_path = remove_leading_slashes(normalized_path)
    
    # Output the final processed path
    print(final_path)

def normalize_path(path):
    """
    Normalize the path by converting backslashes to forward slashes
    and removing unnecessary segments.
    """
    # Replace backslashes with forward slashes
    normalized_path = path.replace("\\", "/")
    
    # Split the path and filter out empty segments
    segments = normalized_path.split("/")
    filtered_segments = [seg for seg in segments if seg not in ("", ".")]  # removing empty and current dir segments
    
    # Deal with parent directory segments
    stack = []
    for segment in filtered_segments:
        if segment == "..":  # If the segment is a parent directory reference
            if stack:
                stack.pop()  # Move up one directory
        else:
            stack.append(segment)  # Regular directory name
    
    # Join the remaining segments together
    return "/".join(stack)

def remove_leading_slashes(path):
    """
    Remove leading slashes, ensuring that only a single leading slash remains.
    """
    if path.startswith('/'):
        # Strip multiple leading slashes and ensure a single leading slash remains
        return '/' + path.lstrip('/')
    return path  # If there's no leading slash, return as it is

if __name__ == "__main__":
    main()
