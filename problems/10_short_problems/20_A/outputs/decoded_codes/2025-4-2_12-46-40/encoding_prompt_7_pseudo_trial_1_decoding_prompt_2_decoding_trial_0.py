def normalize_and_print_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_path = input().strip()

    # Normalize the file path to remove unnecessary components
    normalized_path = normalize(input_path)

    # Replace any occurrences of multiple leading slashes with a single slash
    final_path = normalized_path.lstrip('/').replace('//', '/').replace('///', '/')

    # Output the final formatted path
    print(final_path)

def normalize(input_path):
    # Normalize the file path by resolving any '..' or '.' references
    parts = input_path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            # Skip empty parts or current directory references
            continue
        elif part == '..':
            # Go up one directory if possible
            if stack:
                stack.pop()
        else:
            # Add the part to the stack
            stack.append(part)

    # Join the normalized parts
    return '/'.join(stack)

# Call the function to execute the path normalization and printing
normalize_and_print_path()
