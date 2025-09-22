# Function to normalize a file path input
def normalize_file_path():
    # Step 1: Read Input
    inputPath = input().strip()  # Capture input and trim whitespace

    # Step 2: Normalize File Path
    # Split the input path by slashes
    path_components = inputPath.split('/')  
    # Filter out any empty components (which occur due to redundant slashes)
    filtered_components = [component for component in path_components if component != '']

    # Combine the filtered components back into a normalized path
    normalizedPath = '/' + '/'.join(filtered_components) if filtered_components else '/'
    
    # Step 3: Output Result
    print(normalizedPath)

# Call the function to execute
normalize_file_path()
