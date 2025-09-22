def normalize_path(path):
    """
    Normalize the path to convert backslashes to forward slashes
    and remove unnecessary segments from the path.
    """
    # Replace backslashes with forward slashes
    path = path.replace('\\', '/')
    
    # Split the path into components to handle '.' and '..'
    components = path.split('/')
    stack = []

    for component in components:
        if component == '' or component == '.':
            # Ignore empty component or current directory symbol
            continue
        elif component == '..':
            # Pop the last directory if it exists (going back in the hierarchy)
            if stack:
                stack.pop()
        else:
            # Add the valid directory to the stack
            stack.append(component)

    # Join back the components to form the normalized path
    normalized = '/'.join(stack)
    return normalized

def remove_leading_slashes(path):
    """
    Ensure that the path starts with only a single leading slash.
    """
    if path.startswith('/'):
        # Remove leading slashes and keep only one
        path = path.lstrip('/')
        return '/' + path
    else:
        return path

# Main program execution
input_string = input()  # Read input from standard input

# Normalize the path to eliminate redundant separators and up-level references
normalized_path = normalize_path(input_string)

# Remove leading slashes, ensuring only a single leading slash remains
final_path = remove_leading_slashes(normalized_path)

# Output the final processed path
print(final_path)
