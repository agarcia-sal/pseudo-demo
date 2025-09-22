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
    # Here we use Python's os.path.normpath to standardize the path.
    import os
    return os.path.normpath(input_path)

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash
    # It uses regular expressions to achieve this
    import re
    return re.sub(r'^\/+', '/', path)

# Start the program
if __name__ == "__main__":
    main()
