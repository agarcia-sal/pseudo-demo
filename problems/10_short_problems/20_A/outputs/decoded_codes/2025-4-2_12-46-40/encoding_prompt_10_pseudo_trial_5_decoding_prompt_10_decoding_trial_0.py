def normalize_path():
    # Step 2: Read Input
    input_path = input()
    
    # Step 3: Clean the Input Path
    # Normalize the path by removing redundant slashes
    normalized_path = '/'.join(part for part in input_path.split('/') if part)
    
    # Step 4: Substitute Leading Slashes
    # Ensure it starts with a single leading slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = '/' + normalized_path
    
    # Step 5: Output the Result
    print(final_path)

# Example usage
if __name__ == "__main__":
    normalize_path()
