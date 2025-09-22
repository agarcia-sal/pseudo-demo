import os

def process_path():
    # Read input from standard input and remove any leading or trailing whitespace
    input_string = input().strip()
    
    # Normalize the input string to remove redundant path separators
    normalized_path = os.path.normpath(input_string)
    
    # Replace any sequences of leading slashes with a single slash in normalized_path
    final_output = normalized_path.lstrip('/').replace('//', '/')
    
    # Output the final processed path
    print(final_output)

# Call the function to execute the path processing
process_path()
