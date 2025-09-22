import os

def normalize_path():
    # Step 1: Read Input
    raw_path = input().strip()  # Accept input and remove any leading/trailing whitespace
    
    # Step 2: Normalize Path
    # Normalize the path to the current OS format using os.path.normpath
    normalized_path = os.path.normpath(raw_path)  
    
    # Step 3: Modify Leading Slashes
    if normalized_path.startswith('/'):
        # Replace any leading slashes with a single forward slash
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 4: Output Result
    print(normalized_path)  # Display the modified path as output

# Call the function to run the normalization
normalize_path()
