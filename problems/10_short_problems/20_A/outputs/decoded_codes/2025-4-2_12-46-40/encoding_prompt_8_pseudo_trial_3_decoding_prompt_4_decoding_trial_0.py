import os

def normalize_path(path: str) -> str:
    # Step 1: Read input and trim whitespace
    trimmed_path = path.strip()
    
    # Step 2: Normalize the file path using os.path.normpath
    normalized_path = os.path.normpath(trimmed_path)
    
    # Step 3: Ensure the path starts with a single forward slash
    if normalized_path.startswith('/'):
        # Replace multiple leading slashes with a single one
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = '/' + normalized_path
    
    # Step 4: Print the final normalized path
    print(final_path)

# Example of reading input and calling the normalization function
if __name__ == "__main__":
    path_input = input()  # Read input path
    normalize_path(path_input)
