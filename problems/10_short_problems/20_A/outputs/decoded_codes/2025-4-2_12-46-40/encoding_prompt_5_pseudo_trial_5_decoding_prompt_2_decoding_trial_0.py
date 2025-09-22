import os

def normalize_file_path():
    # Step 1: Read the file path from standard input
    file_path = input().strip()  # Removes any extra spaces
    
    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(file_path)  # Use os library to handle system path conventions
    
    # Step 3: Remove leading slashes
    final_path = normalized_path.lstrip('/')  # Removes all leading slashes
    final_path = '/' + final_path if final_path else final_path  # Add a single leading slash if final_path is not empty

    # Step 4: Output the result
    print(final_path)

# Call the function to execute
normalize_file_path()
