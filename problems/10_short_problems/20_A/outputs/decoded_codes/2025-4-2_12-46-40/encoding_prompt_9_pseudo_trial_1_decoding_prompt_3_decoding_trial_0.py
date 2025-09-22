import os

def normalize_path():
    # Step 2: Receive Input
    user_input = input().strip()
    
    # Step 3: Normalize Path
    # Using os.path.normpath to clean up the path
    normalized_path = os.path.normpath(user_input)
    
    # Step 4: Ensure Single Leading Slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Output Result
    print(normalized_path)

# Call the function to execute the program
normalize_path()
