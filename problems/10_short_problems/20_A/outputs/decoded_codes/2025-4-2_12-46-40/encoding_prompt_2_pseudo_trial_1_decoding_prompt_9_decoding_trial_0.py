# Function to normalize a file path
def normalize_file_path():
    # Read input
    file_path = input().strip()  # Obtain user input and remove leading/trailing spaces
    
    # Normalize the file path
    # Remove any extra leading slashes and ensure there is one leading slash
    while file_path.startswith('/'):
        file_path = file_path[1:]  # Remove leading slash

    # Add a leading slash if the path is not empty now
    if file_path:
        file_path = '/' + file_path

    # Output the result
    print(file_path)

# Start the normalization process
normalize_file_path()
