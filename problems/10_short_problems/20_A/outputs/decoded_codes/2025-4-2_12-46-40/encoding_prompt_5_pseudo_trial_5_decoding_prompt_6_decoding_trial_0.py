import os

def normalize_file_path():
    # STEP 1: Read the file path from standard input and remove extra spaces
    file_path = input().strip()

    # STEP 2: Normalize the file path using system path conventions
    normalized_path = os.path.normpath(file_path)

    # STEP 3: Remove leading slashes and ensure single leading slash
    final_path = '/' + normalized_path.lstrip('/')

    # STEP 4: Output the result
    print(final_path)

# Call the function to execute the normalization
normalize_file_path()
