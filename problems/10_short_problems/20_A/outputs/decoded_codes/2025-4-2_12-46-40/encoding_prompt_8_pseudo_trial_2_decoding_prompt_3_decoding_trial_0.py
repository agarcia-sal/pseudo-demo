def main():
    # Step 1: Read the input file path from standard input
    user_input = input()
    
    # Step 2: Normalize the input path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Ensure the normalized path starts with a single '/'
    final_path = replace_multiple_leading_slashes(normalized_path)
    
    # Step 4: Print the final normalized path
    print(final_path)

def normalize_path(input_path: str) -> str:
    """
    Normalize the input path by removing redundant separators and up-level references.
    """
    # Split the path into components, remove unnecessary ones and filter out empty components
    components = input_path.split('/')
    filtered_components = []
    
    for component in components:
        if component == '' or component == '.':
            continue
        if component == '..':
            if filtered_components:
                filtered_components.pop()  # Go one level up
        else:
            filtered_components.append(component)

    # Join the filtered components back into a normalized path
    normalized_input_path = '/'.join(filtered_components)
    return normalized_input_path

def replace_multiple_leading_slashes(path: str) -> str:
    """
    Ensure the path starts with a single leading '/'.
    """
    if path.startswith('/'):
        # Replace any leading slashes with a single slash
        return '/' + path.lstrip('/')
    else:
        # Prepend a single slash if none exists
        return '/' + path

# Run the main function
main()
