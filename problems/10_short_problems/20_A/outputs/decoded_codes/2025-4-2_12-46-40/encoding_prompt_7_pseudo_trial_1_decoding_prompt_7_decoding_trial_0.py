def normalize_and_print_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace any leading multiple slashes with a single slash
    final_path = replace_multiple_leading_slashes(normalized_path)

    # Output the final formatted path
    print(final_path)

def normalize(input_path):
    # Split the path into components and initialize a list for normalized components
    components = input_path.split('/')
    normalized_components = []

    for component in components:
        if component == '' or component == '.':
            # Skip empty components (due to leading/trailing slashes) and current directory references
            continue
        elif component == '..':
            # Remove the last valid component if we encounter a parent directory reference
            if normalized_components:
                normalized_components.pop()
        else:
            # Add valid components to the normalized list
            normalized_components.append(component)
    
    # Join normalized components back into a path with a single slash
    return '/' + '/'.join(normalized_components)

def replace_multiple_leading_slashes(normalized_path):
    # Use regular expression to replace multiple leading slashes
    import re
    return re.sub(r'^/+', '/', normalized_path)  # Replace multiple leading slashes with a single slash

# Invoke the function to run the normalization and path printing
normalize_and_print_path()
