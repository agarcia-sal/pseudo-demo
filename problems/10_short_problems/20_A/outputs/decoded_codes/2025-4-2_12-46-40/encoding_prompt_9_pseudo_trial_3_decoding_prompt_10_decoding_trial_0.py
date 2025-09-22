def normalize_file_path():
    # Step 1: Receive Input
    file_path = input().strip()  # Read input and remove leading/trailing whitespace
    
    # Step 2: Normalize the File Path
    # Split the file path by the '/' character, effectively breaking it into components
    path_components = file_path.split('/')
    
    # Filter out any empty components to resolve redundant path elements
    normalized_components = [component for component in path_components if component]
    
    # Step 3: Adjust the Path
    # Join the components back together using '/', ensuring the path is normalized
    normalized_path = '/'.join(normalized_components)
    
    # Ensure that the final path starts with a single root slash
    if normalized_path:
        final_path = '/' + normalized_path
    else:
        final_path = '/'  # Handle case where input was just slashes or empty
    
    # Step 4: Output the Result
    print(final_path)

# Call the function to execute the file path normalization
normalize_file_path()
