def normalize_file_path():
    # Step 1: Read input and remove leading/trailing whitespace
    raw_input = input().strip()
    
    # Step 2: Normalize path
    # We will replace backslashes with forward slashes and split the path
    parts = raw_input.replace('\\', '/').split('/')
    normalized_parts = []
    
    for part in parts:
        if part and part != '.':
            normalized_parts.append(part)
    
    # Step 3: Join the normalized parts with a single forward slash
    normalized_path = '/'.join(normalized_parts)
    
    # Step 4: Modify leading slashes
    if normalized_path.startswith('/'):
        # Replace leading slashes with a single slash
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Output the result
    print(normalized_path)

# Execute the function
normalize_file_path()
