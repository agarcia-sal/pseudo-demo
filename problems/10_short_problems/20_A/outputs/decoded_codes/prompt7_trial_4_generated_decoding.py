def normalize_and_sanitize_path():
    # Read input from standard input
    input_path = input()
    
    # Normalize the path by removing any redundant separators and up-level references
    normalized_path = normalize(input_path)
    
    # Replace any leading slashes with a single leading slash
    sanitized_path = replace_leading_slashes(normalized_path)
    
    # Output the sanitized path
    print(sanitized_path)

def normalize(input_path):
    # Split the path into components based on the slash separator
    components = input_path.split('/')
    
    # Create a stack to build the normalized path
    stack = []
    
    # Process each component
    for part in components:
        # Skip empty components resulting from leading/trailing slashes
        if part == '' or part == '.':
            continue
        # Handle up-level references
        elif part == '..':
            if stack:  # Only pop if there is something to go up to
                stack.pop()
        else:
            # If it's a valid directory name, push onto the stack
            stack.append(part)
    
    # Join the normalized components into a single string
    normalized_path = '/'.join(stack)
    
    # Return the normalized path - if empty, return a single dot
    return normalized_path if normalized_path else '.'

def replace_leading_slashes(normalized_path):
    # If the normalized path has multiple leading slashes, replace them
    if normalized_path.startswith('/'):
        # Keep only the first slash
        return '/' + normalized_path.lstrip('/')
    else:
        return normalized_path

# Execute the function to normalize and sanitize the path
normalize_and_sanitize_path()
