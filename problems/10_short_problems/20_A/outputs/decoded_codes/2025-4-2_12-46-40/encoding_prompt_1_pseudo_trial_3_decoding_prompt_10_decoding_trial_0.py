import os

def clean_path_input():
    # Step 1: Read the input path and trim whitespace
    path_string = input().strip()  # Read input and remove leading/trailing whitespace

    # Step 2: Normalize the path using the file system conventions
    normalized_path = os.path.normpath(path_string)  # Normalize the path

    # Step 3: Replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        # Count leading slashes and replace with a single slash
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path

    # Step 4: Output the final cleaned path
    print(cleaned_path)

# Call the function to execute the path cleaning process
clean_path_input()
