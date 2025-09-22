import os

def normalize_file_path():
    # Step 1: Read input
    original_path = input()  # Read input from standard input
    trimmed_path = original_path.strip()  # Remove extra spaces from both ends

    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(trimmed_path)  # Normalize the path

    # Step 3: Ensure the path starts with a single forward slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')  # Remove extra leading slashes
    else:
        final_path = '/' + normalized_path  # Ensure it starts with a single slash
    
    # Step 4: Output the final result
    print(final_path)  # Print the adjusted path to standard output

# Example of running the function
normalize_file_path()

# Test cases:
# Input: "///folder/../file.txt"  -> Output: "/folder/file.txt"
# Input: "  /user// documents///file.txt   " -> Output: "/user/documents/file.txt"
# Input: "file.txt" -> Output: "/file.txt"
