def normalize_file_path():
    # Receive Input
    file_path = input().strip()  # Read input and remove leading/trailing whitespace
    
    # Normalize the File Path
    # Split the path by slashes and filter out unnecessary components
    path_components = file_path.split('/')
    filtered_components = [component for component in path_components if component and component != '.']
    
    # Construct the normalized path
    normalized_path = '/'.join(filtered_components)

    # Adjust the Path
    final_path = '/' + normalized_path if normalized_path else '/'
    
    # Handle leading slashes
    if final_path.startswith('//'):
        final_path = '/' + final_path.lstrip('/')
    
    # Output the Result
    print(final_path)

# Call the function to execute the normalization
normalize_file_path()
