def read_input():
    """Read the entire input from standard input and trim leading/trailing spaces."""
    return input().strip()

def normalize_path(input_path):
    """Normalize the input path by removing redundant separators and up-level references."""
    # Split the path into components
    components = input_path.split('/')
    stack = []

    for component in components:
        if component == '' or component == '.':
            # Ignore empty components (redundant slashes) and current directory references
            continue
        elif component == '..':
            # Go up one level in the directory
            if stack:
                stack.pop()
        else:
            # Valid directory name, add to stack
            stack.append(component)

    # Join the components back into a normalized path
    return '/'.join(stack)

def format_path(normalized_path):
    """Format the normalized path to ensure it has no leading slashes."""
    # Start with the normalized path and remove leading slashes
    return normalized_path.lstrip('/')

def main():
    """Main execution flow to read, normalize, format, and output the path."""
    # Step 1: Read the input path
    input_path = read_input()
    
    # Step 2: Normalize the path
    normalized_path = normalize_path(input_path)
    
    # Step 3: Format the path
    formatted_path = format_path(normalized_path)

    # Output the final formatted path
    print(formatted_path)

if __name__ == "__main__":
    main()
