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
    # Remove redundant elements (this implementation is basic)
    normalized = input_path.replace("//", "/")  # This can handle double slashes
    return normalized

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash
    while path.startswith("/"):
        path = path[1:]  # Remove the leading slash
    return "/" + path  # Add a single leading slash back

# Start the program
main()
