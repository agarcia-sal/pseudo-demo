def normalize(input_path):
    """
    Normalize the file path by converting it to a standard format.
    This involves resolving any '..' (parent directory) or '.' (current directory) references.
    """
    # Split the path into components and filter out empty segments
    components = input_path.split('/')
    stack = []
    
    for part in components:
        if part == '' or part == '.':
            # Ignore empty segments and current directory references
            continue
        elif part == '..':
            # Go up one directory if possible
            if stack:
                stack.pop()
        else:
            # Add valid segments to the stack
            stack.append(part)

    # Join the stack into a normalized path
    return '/'.join(stack)

def normalize_and_print_path():
    """
    Read a file path from the user input, normalize it,
    replace any leading slashes with a single slash, and print the result.
    """
    # Read the input and remove any leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the file path
    normalized_path = normalize(input_path)
    
    # Replace multiple leading slashes with a single slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path.lstrip('/')
    
    # Output the final formatted path
    print(final_path)

# Example call to the function (you can uncomment it to run)
# normalize_and_print_path()
