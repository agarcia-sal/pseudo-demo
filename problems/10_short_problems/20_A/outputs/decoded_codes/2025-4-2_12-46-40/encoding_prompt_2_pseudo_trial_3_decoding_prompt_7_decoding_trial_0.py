# Function to normalize the file path by cleaning up irregular formatting
def normalize_path(path):
    # Remove any surrounding spaces from the input path
    path = path.strip()
    
    # Normalize by replacing multiple leading slashes with a single slash
    if path.startswith('/'):
        # Replace leading slashes with a single slash using a while loop
        while path.startswith('//'):
            path = path[1:]  # Remove one leading slash
    # Ensure that the path starts with a single forward slash
    if not path.startswith('/'):
        path = '/' + path
    
    return path

# Main execution begins here
if __name__ == "__main__":
    # Read the file path input from standard input
    input_path = input()
    
    # Normalize the input path
    normalized_path = normalize_path(input_path)
    
    # Output the cleaned-up path
    print(normalized_path)
