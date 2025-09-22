import os

def process_path():
    # Read input path from standard input
    input_path = input().strip()
    
    # Normalize the input path using POSIX standards
    normalized_path = os.path.normpath(input_path)
    
    # Remove leading slashes, ensuring at least one leading slash remains
    if normalized_path.startswith("/"):
        # If there's a leading slash, strip it and re-add a single leading slash
        result_path = "/" + normalized_path.lstrip("/")
    else:
        # If there's no leading slash, just ensure at least one leading slash is present
        result_path = "/" + normalized_path
    
    # Output the final processed path
    print(result_path)

# Run the function to process the path
process_path()
