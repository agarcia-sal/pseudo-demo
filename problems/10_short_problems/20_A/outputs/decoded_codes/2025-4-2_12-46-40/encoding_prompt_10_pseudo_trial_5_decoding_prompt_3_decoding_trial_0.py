def normalize_path():
    # Read input from the user
    input_path = input()
    
    # Clean the input path by normalizing it
    # This will remove redundant slashes
    normalized_path = "/".join(part for part in input_path.split("/") if part)
    
    # Substitute leading slashes with a single leading slash
    if normalized_path:
        final_path = "/" + normalized_path
    else:
        final_path = "/"
    
    # Output the final normalized path
    print(final_path)

# Call the function to execute the path normalization
normalize_path()
