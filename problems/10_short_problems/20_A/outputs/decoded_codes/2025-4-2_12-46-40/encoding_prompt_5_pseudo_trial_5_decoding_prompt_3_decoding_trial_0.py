import os  # Import the os library for path normalization

def normalize_file_path():
    # STEP 1: Read the file path from standard input and remove extra spaces
    file_path = input().strip()

    # STEP 2: Normalize the file path using system path conventions
    normalized_path = os.path.normpath(file_path)

    # STEP 3: Remove leading slashes and ensure only a single leading slash remains
    # This will replace all leading slashes with one single slash
    final_path = '/' + normalized_path.lstrip('/')

    # STEP 4: Output the result
    print(final_path)

# Now the function can be tested by calling it
normalize_file_path()
