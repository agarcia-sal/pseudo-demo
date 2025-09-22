def main():
    # Read input from standard input and remove extra spaces
    input_path = input().strip()
    
    # Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Replace any sequence of leading slashes with a single slash
    final_path = replace_leading_slashes(normalized_path)
    
    # Output the final normalized path
    print(final_path)

def normalize_path(input_path):
    # This function transforms the file path to a standard format
    # Implementation details depend on specific requirements for normalization
    # Here we can assume normalization could include transforming to absolute path, resolving '.' and '..', etc.
    # For demonstration purposes, we're just returning the input path as is
    return input_path  # Placeholder for real normalization logic

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        # Remove the leading slash from path
        path = path[1:]
    
    # Return the path with a single leading slash
    return '/' + path if path else path  # Ensures we return an empty string or a valid path

# Call the main function to execute the program
main()
