import os

def normalize_file_path():
    # STEP 1: Read the file path from standard input
    file_path = input().strip()  # Removing any extra spaces

    # STEP 2: Normalize the file path using system path conventions
    normalized_path = os.path.normpath(file_path)

    # STEP 3: Remove leading slashes by replacing them with a single slash
    final_path = normalized_path.lstrip('/')

    # Adding the leading slash back to maintain a standard format for the final path
    final_path = '/' + final_path if final_path else final_path

    # STEP 4: Output the result
    print(final_path)

# Call the function to execute
normalize_file_path()
