def normalize_path(input_path):
    # This function normalizes the given file path.
    # Replace with implementation for normalization
    return input_path  # Placeholder for actual normalization logic

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash.
    while path.startswith('/'):
        path = path[1:]
    return '/' + path if path else '/'  # Ensures at least one slash

def main():
    # Step 1: Read input from the standard input (user)
    user_input = input()
    
    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Adjust leading slashes
    if normalized_path.startswith('/'):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)

    # Step 4: Output the final normalized path
    print(normalized_path)

# Start the program
if __name__ == "__main__":
    main()
