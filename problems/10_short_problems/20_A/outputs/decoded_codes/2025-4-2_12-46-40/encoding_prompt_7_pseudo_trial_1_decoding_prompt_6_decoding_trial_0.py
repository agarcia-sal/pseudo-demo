def normalize_and_print_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)
    
    # Replace any occurrences of multiple leading slashes with a single slash in normalized_path
    final_path = normalized_path.lstrip('/')  # removes leading slashes, keeping one
    
    # Output the final formatted path
    print(final_path)

def normalize(input_path):
    # Normalize the file path by resolving any '..' or '.' references in the path
    # This is a simple representation of normalization
    import os
    return os.path.normpath(input_path)

# Call the main function to execute the program
normalize_and_print_path()
