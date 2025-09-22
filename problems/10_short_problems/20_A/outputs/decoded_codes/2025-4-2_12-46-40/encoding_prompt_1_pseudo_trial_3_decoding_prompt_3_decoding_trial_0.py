import os

def normalize_and_clean_path():
    # Step 1: Read input path string and trim whitespace
    path_string = input().strip()
    
    # Step 2: Normalize the path using the built-in os.path functionality
    normalized_path = os.path.normpath(path_string)

    # Step 3: Replace multiple leading slashes with a single leading slash
    # Check the beginning of the normalized path for leading slashes
    if normalized_path.startswith('/'):
        # Replace consecutive leading slashes with a single slash
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path.lstrip('/')

    # Step 4: Output the final cleaned path
    print(cleaned_path)

# To execute the function, uncomment the following line
# normalize_and_clean_path()
