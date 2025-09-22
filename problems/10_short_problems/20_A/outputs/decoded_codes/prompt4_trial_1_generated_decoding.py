import os

def normalize_path():
    # Read the input and remove extra spaces
    input_path = input().strip()
    
    # Normalize the input path using os.path.normpath to handle any irregularities
    normalized_path = os.path.normpath(input_path)
    
    # Replace any leading slashes with a single slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path
    
    # Output the resulting normalized path
    print(final_path)

# Call the function to execute
normalize_path()
