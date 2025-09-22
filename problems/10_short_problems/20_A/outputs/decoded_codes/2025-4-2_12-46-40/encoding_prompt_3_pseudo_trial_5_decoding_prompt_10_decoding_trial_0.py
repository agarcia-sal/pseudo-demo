def read_input():
    """Reads input from standard input and removes leading/trailing spaces."""
    return input().strip()

def normalize_path(input_path):
    """Normalizes the path by removing redundant separators and up-level references."""
    # Split the path by '/' and handle normalization
    parts = input_path.split('/')
    normalized_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            # Skip empty parts (redundant slashes) and current directory references
            continue
        if part == '..':
            # Handle up-level directory references
            if normalized_parts:
                normalized_parts.pop()  # Remove the last valid directory if possible
        else:
            # Add valid directory names
            normalized_parts.append(part)

    # Join normalized parts into a single path
    return '/' + '/'.join(normalized_parts) if normalized_parts else '/'

def format_path(normalized_path):
    """Formats the path by ensuring there are no leading slashes beyond the first."""
    return normalized_path.lstrip('/')

def main():
    """Main execution flow of the program."""
    # Read input path
    input_path = read_input()
    
    # Normalize the path
    normalized_path = normalize_path(input_path)
    
    # Format the path
    formatted_path = format_path(normalized_path)

    # Output the final formatted path
    print(formatted_path)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()


# Test cases for the path normalization and formatting functions
assert main_input() == '/a/b'
assert main_input() == '/a/b/c'
assert main_input() == '/'
assert main_input() == '/a'
assert main_input() == '/b/a'
assert main_input() == '/a'
assert main_input() == '/b'
assert main_input() == '/a/b'
