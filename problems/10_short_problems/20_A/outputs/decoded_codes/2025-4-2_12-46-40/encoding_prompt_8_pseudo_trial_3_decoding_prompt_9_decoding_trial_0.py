import os

def normalize_file_path(path):
    # Normalize the path by resolving any '..' and '.' within it
    normalized_path = os.path.normpath(path)
    return normalized_path

def main():
    # Step 1: Read input and trim whitespace
    original_path = input()
    trimmed_path = original_path.strip()

    # Step 2: Normalize the file path
    normalized_path = normalize_file_path(trimmed_path)

    # Step 3: Ensure the path starts with a single forward slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = '/' + normalized_path
    
    # Step 4: Output the final result
    print(final_path)

# Call main function
main()
