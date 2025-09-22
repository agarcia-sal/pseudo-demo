import os

def normalize_path():
    # Step 2: Read input path from the user
    user_input = input().strip()
    
    # Step 3: Normalize the path using os.path.normpath
    normalized_path = os.path.normpath(user_input)
    
    # Step 4: Ensure that the path starts with a single leading slash
    if normalized_path.startswith("//"):
        normalized_path = "/" + normalized_path.lstrip("/")
    
    # Step 5: Output the final normalized path
    print(normalized_path)

# Example usage; uncomment to run the function
# normalize_path()
