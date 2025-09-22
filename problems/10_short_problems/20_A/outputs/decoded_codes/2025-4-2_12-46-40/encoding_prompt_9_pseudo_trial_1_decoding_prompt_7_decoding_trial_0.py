def normalize_path(path):
    # Split the path into components based on slashes
    components = path.split('/')
    
    # Use a list to maintain a stack for the normalized path
    stack = []
    
    for component in components:
        # Ignore empty components and current directory references
        if component == '' or component == '.':
            continue
        # If it's a parent directory reference, pop the last valid component
        elif component == '..':
            if stack:
                stack.pop()  # Remove the last component if possible
        else:
            # Add valid components to the stack
            stack.append(component)
    
    # Join the stack components with slashes to form the normalized path
    normalized_path = '/'.join(stack)
    
    # If the normalized path starts with multiple slashes, replace them with a single slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # If the stack is empty, it means we are at the root
    return '/' + normalized_path if normalized_path else '/'

def main():
    # Read input data as a string from the standard input
    user_input = input().strip()  # Remove whitespace

    # Normalize the input path
    normalized_path = normalize_path(user_input)

    # Output the final normalized path
    print(normalized_path)

# Start the program
if __name__ == "__main__":
    main()
