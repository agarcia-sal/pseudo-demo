def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = "/".join(part for part in input_path.split("/") if part)
    
    # Replace any leading slashes with a single slash
    formatted_path = normalized_path.lstrip("/")
    
    # Output the formatted path
    print(formatted_path)

# For testing purpose
# Uncomment below lines to test the function
# normalize_and_format_path()  # should call the function to test it
