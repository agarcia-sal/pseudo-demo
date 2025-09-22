import os

def normalize_and_clean_file_path():
    # Step 2: Input Handling
    input_string = input()
    
    # Step 3: Process Input
    # Remove leading/trailing whitespaces
    trimmed_path = input_string.strip()
    
    # Normalize File Path
    normalized_path = os.path.normpath(trimmed_path)
    
    # Step 4: Clean Path
    # Substitute multiple leading slashes with a single slash
    cleaned_path = normalized_path.lstrip('/').replace('//', '/')
    
    # Prepend a single slash if the cleaned path is not empty
    if cleaned_path:
        cleaned_path = '/' + cleaned_path
    
    # Step 5: Output Result
    print(cleaned_path)

# Start the execution of the program
normalize_and_clean_file_path()
