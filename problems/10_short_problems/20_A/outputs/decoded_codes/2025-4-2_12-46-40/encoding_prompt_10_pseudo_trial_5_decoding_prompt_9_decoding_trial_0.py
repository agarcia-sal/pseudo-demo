def normalize_path():
    # Step 2: Read input from the user
    input_path = input()
    
    # Step 3: Clean the input path
    # Normalize the path by removing redundant slashes
    normalized_path = "/".join(part for part in input_path.split("/") if part)
    
    # Step 4: Substitute leading slashes
    if normalized_path.startswith("/"):
        final_path = "/" + normalized_path.lstrip("/")
    else:
        final_path = "/" + normalized_path
    
    # Step 5: Output the result
    print(final_path)

# Execute the main procedure
normalize_path()
