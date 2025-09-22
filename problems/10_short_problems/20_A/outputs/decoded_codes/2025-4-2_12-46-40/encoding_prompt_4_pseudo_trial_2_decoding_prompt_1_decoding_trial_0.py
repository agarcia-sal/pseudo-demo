def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()  # Using .strip() to remove extra whitespace
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = normalize(input_path)  # Assuming there is a function to normalize the path
    
    # Replace any leading slashes with a single slash
    formatted_path = normalized_path.lstrip('/')  # lstrip to remove leading slashes
    if formatted_path and formatted_path[0] != '/':
        formatted_path = '/' + formatted_path  # Add a single leading slash if the path isn't empty
    
    # Output the formatted path
    print(formatted_path)

# Note: The actual normalization logic has to be implemented, which typically 
# involves handling various filesystem-specific details or ambiguous path segments.
