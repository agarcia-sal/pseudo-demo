import os

def normalize_file_path():
    # Step 1: Read input
    original_path = input().strip()  # Remove extra whitespace from both ends of original_path
    
    # Step 2: Normalize the file path
    # This can be done by using os.path.normpath which will handle redundant separators and up-level references
    normalized_path = os.path.normpath(original_path)
    
    # Step 3: Ensure the path starts with a single forward slash
    # We can use lstrip to remove leading slashes and then add a single one
    final_path = '/' + normalized_path.lstrip('/')
    
    # Step 4: Output the final result
    print(final_path)

# Call the function to execute the code
normalize_file_path()
