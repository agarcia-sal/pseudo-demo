def normalize_file_path():
    # Read input from standard input (a single string representing a file path)
    input_path = input().strip()  # Step 1 and 2: Read and trim whitespace

    # Step 3: Normalize the input_path
    # a. Replace all backslashes with forward slashes
    normalized_path = input_path.replace("\\", "/")
    
    # b. Collapse multiple consecutive forward slashes into a single one
    normalized_path = normalized_path.replace("//", "/")
    
    # Handle cases where multiple slashes may exist due to the previous step
    while "//" in normalized_path:
        normalized_path = normalized_path.replace("//", "/")

    # c. Ensure no leading slash unless the path is the root
    if normalized_path.startswith("/") and not normalized_path.startswith("//"):
        normalized_path = normalized_path[1:]  # Remove the leading slash if unnecessary

    # Step 4: Output the normalized path
    print(normalized_path)

# This would invoke the function to process input and normalize the path
normalize_file_path()
