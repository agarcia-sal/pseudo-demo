def read_input():
    """Read input data from standard input and remove leading/trailing spaces."""
    return input().strip()

def normalize_path(input_path):
    """Normalize the input path by removing redundant separators and up-level references."""
    parts = input_path.split('/')  # Split the path by slashes
    stack = []  # Use a stack to manage the directory components
    
    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts and current directory references
        elif part == '..':
            if stack:
                stack.pop()  # Remove the last directory for up-level reference
        else:
            stack.append(part)  # Add the directory to the stack
    
    # Join the stack to create the normalized path
    normalized_path = '/' + '/'.join(stack)
    return normalized_path

def format_path(normalized_path):
    """Format the normalized path by removing any leading slashes."""
    return normalized_path.lstrip('/')

def main():
    """Main execution flow."""
    # Read input path
    input_path = read_input()
    
    # Normalize the path
    normalized_path = normalize_path(input_path)
    
    # Format the path
    formatted_path = format_path(normalized_path)

    # Output the final formatted path
    print(formatted_path)

# You can test the functions with some test cases
# Example test cases
# Input: '///usr//bin//../bin/./scripts//'
# Output: 'usr/bin/scripts'
# Input: '/home/../user/./documents//'
# Output: 'user/documents'
