import os

def normalize_file_path():
    # Step 1: Read the input
    input_path = input()
    
    # Step 2: Normalize the path
    normalized_path = os.path.normpath(input_path).replace('\\', '/')

    # Step 3: Remove leading slashes
    final_path = '/' + normalized_path.lstrip('/')

    # Step 4: Print the resulting path
    print(final_path)

# Main execution
normalize_file_path()
