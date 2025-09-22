def main():
    # Step 1: Read input from the user
    user_input = input()
    
    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Adjust leading slashes
    if normalized_path.startswith("/"):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)

    # Step 4: Output the final normalized path
    print(normalized_path)

def normalize_path(input_path):
    # This function normalizes the given file path
    # Split the path by the forward slash
    path_parts = input_path.split("/")
    # Remove unnecessary elements (like empty parts caused by consecutive slashes)
    normalized_parts = [part for part in path_parts if part]
    # Join the normalized parts back together, ensuring a single slash between them
    normalized_path = "/" + "/".join(normalized_parts)
    return normalized_path

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash
    while path.startswith("/"):
        path = path[1:]
    return "/" + path  # Ensures there's one leading slash

# Call main to execute the program
main()
