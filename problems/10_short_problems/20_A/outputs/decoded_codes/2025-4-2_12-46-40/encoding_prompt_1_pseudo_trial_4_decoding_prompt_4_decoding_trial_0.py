def normalize_file_path():
    # Step 1: Read input from standard input and trim whitespace
    input_path = input().strip()

    # Step 2: Normalize the file path
    # Split the path into components, removing empty ones caused by redundant slashes
    components = input_path.split('/')
    filtered_components = [component for component in components if component]

    # Join the filtered components with a single forward slash
    normalized_path = '/' + '/'.join(filtered_components)

    # Step 3: Output the normalized path
    print(normalized_path)

# If this module is the main program, run the function
if __name__ == "__main__":
    normalize_file_path()
