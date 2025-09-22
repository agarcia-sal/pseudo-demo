def normalize_file_path_and_print(input_string):
    # Remove leading and trailing whitespace from input_string
    cleaned_input = input_string.strip()
    
    # Normalize the file path using a standard format
    # (In this case, we assume normalization involves converting it to a standard form)
    normalized_path = cleaned_input.replace('\\', '/')
    
    # Replace any occurrences of multiple leading slashes with a single leading slash
    while '//' in normalized_path:
        normalized_path = normalized_path.replace('//', '/')

    # Print the formatted file path
    print(normalized_path)

# Main execution block
input_string = input()
normalize_file_path_and_print(input_string)
