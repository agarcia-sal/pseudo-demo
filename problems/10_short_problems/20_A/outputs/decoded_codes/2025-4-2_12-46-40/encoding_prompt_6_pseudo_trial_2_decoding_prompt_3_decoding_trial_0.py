def normalize_path(input_path):
    """
    Normalize the file path to a standard format.
    This function should implement specific normalization requirements.
    """
    # Implementation details for normalization can be specified here.
    # For demonstration, we will just return the input path as is.
    # Modify this based on actual normalization rules needed.
    return input_path

def replace_leading_slashes(path):
    """
    Replace sequences of leading slashes at the start of the path
    with a single leading slash.
    """
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash back

def main():
    # Read input from standard input and remove extra spaces
    input_path = input().strip()
    
    # Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Replace any sequence of leading slashes with a single slash
    final_path = replace_leading_slashes(normalized_path)
    
    # Output the final normalized path
    print(final_path)

# Run the program
if __name__ == "__main__":
    main()
