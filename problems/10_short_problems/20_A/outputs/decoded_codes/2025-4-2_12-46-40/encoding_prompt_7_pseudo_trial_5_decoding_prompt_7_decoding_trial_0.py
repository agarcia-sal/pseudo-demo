def normalize_file_path_and_print(input_string):
    # REMOVE leading and trailing whitespace from input_string
    cleaned_input = input_string.strip()
    
    # NORMALIZE the file path using a standard format
    # This simplifies the path, for instance, by reducing consecutive slashes
    normalized_path = cleaned_input.replace("\\", "/")  # Convert backslashes to slashes for consistency
    normalized_path = normalized_path.split('/')  # Split path by slashes
    
    # FILTER out any empty segments after the split and handle multiple leading slashes
    formatted_path = [segment for segment in normalized_path if segment]  # Remove empty segments
    if formatted_path:
        # Join segments back into a path with a single leading slash
        formatted_path = '/' + '/'.join(formatted_path)
    else:
        formatted_path = '/'  # Handle the case where the input could lead to an empty path

    # PRINT the formatted file path
    print(formatted_path)

# MAIN EXECUTION BLOCK
input_string = input()  # Read input from standard input
normalize_file_path_and_print(input_string)  # Call the function with the input
