import re

def main():
    # Read input from standard input
    raw_input = input()
    
    # Normalize the file path to remove any redundant separators
    normalized_path = normalize_path(raw_input)
    
    # Use a regular expression to ensure the path starts with a single '/'
    final_path = remove_leading_slashes(normalized_path, 1)
    
    # Output the final formatted file path
    print(final_path)

def normalize_path(input_path):
    """
    Normalize the input path by resolving relative paths and removing unnecessary separators.
    This function can be extended to handle specific scenarios as needed.
    """
    # Replace multiple slashes with a single slash
    normalized = re.sub(r'/+', '/', input_path)
    
    # Handle relative path components like "./" and "../"
    parts = normalized.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts and current directory references
        if part == '..':
            if stack:
                stack.pop()  # Remove the last valid directory for parent reference
        else:
            stack.append(part)  # Add valid directory to stack
    
    # Join the stack into a normalized path
    return '/' + '/'.join(stack)

def remove_leading_slashes(path, retain_count):
    """
    Replace multiple leading slashes with a single slash, retaining the desired number of leading slashes.
    """
    # This regex replaces multiple leading slashes with a single one,
    # retaining the specified count of leading slashes
    leading_slashes = re.match(r'(/+)', path)
    if leading_slashes:
        # If there are leading slashes, only keep the first 'retain_count'
        return '/' + path.lstrip('/')
    else:
        return path

# Running the main function to execute the code
if __name__ == '__main__':
    main()
