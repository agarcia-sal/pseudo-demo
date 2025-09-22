def normalize_path():
    # Step 1: Read the input string and strip surrounding spaces
    input_path = input().strip()
    
    # Step 2: Normalize the path to cleaner formatting
    # This can be a simple replacement process for slashes
    normalized_path = input_path.replace("\\", "/")  # Change backslashes to forward slashes

    # Step 3: Replace leading forward slashes with a single forward slash
    while normalized_path.startswith("//"):
        normalized_path = normalized_path[1:]  # Remove the first slash until one remains

    # Ensure that there is at least one leading slash
    if not normalized_path.startswith("/"):
        normalized_path = "/" + normalized_path
    
    # Step 4: Output the cleaned-up path
    print(normalized_path)

# Testing
normalize_path()
