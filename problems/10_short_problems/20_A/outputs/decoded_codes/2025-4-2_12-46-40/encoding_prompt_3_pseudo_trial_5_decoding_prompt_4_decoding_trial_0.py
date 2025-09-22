def read_input():
    """Read the entire input from standard input and strip leading/trailing spaces."""
    return input().strip()

def normalize_path(input_path):
    """Normalize the path by removing redundant separators and up-level references."""
    # Split the path by slashes and filter out empty components
    components = input_path.split('/')
    normalized_components = []

    for component in components:
        if component == '' or component == '.':
            continue  # Skip empty components and current directory references
        if component == '..':
            if normalized_components:
                normalized_components.pop()  # Remove the last component for up-level reference
        else:
            normalized_components.append(component)  # Keep valid components

    # Join the components back into a normalized path
    normalized_path = '/' + '/'.join(normalized_components)
    return normalized_path

def format_path(normalized_path):
    """Format the normalized path by removing any leading slashes."""
    return normalized_path.lstrip('/')

def main():
    """Main execution flow of the program."""
    # Step 1: Read input path
    input_path = read_input()
    
    # Step 2: Normalize the path
    normalized_path = normalize_path(input_path)
    
    # Step 3: Format the path
    formatted_path = format_path(normalized_path)

    # Step 4: Output the final formatted path
    print(formatted_path)

# Execute main function
if __name__ == "__main__":
    main()
