def normalize_path(path):
    # Convert backslashes to forward slashes and remove unnecessary segments
    path = path.replace('\\', '/')  # Normalize backslashes to forward slashes
    parts = path.split('/')  # Split the path on forward slashes
    stack = []

    for part in parts:
        if part == '' or part == '.':
            # Skip empty parts (redundant slashes) and current directory references
            continue
        elif part == '..':
            # Go up one directory level if possible
            if stack:
                stack.pop()  # Remove the last directory added to the stack
        else:
            # Add the directory part to the stack
            stack.append(part)

    # Join the stack to form the normalized path
    normalized_path = '/'.join(stack)
    return normalized_path


def remove_leading_slashes(path):
    if path.startswith('/'):
        return '/' + path.lstrip('/')  # Replace leading slashes with a single leading slash
    return path  # Return the path unchanged if no leading slashes exist


# Main execution starts here
input_string = input()  # Read input from the standard input
normalized_path = normalize_path(input_string)  # Normalize the path
final_path = remove_leading_slashes(normalized_path)  # Remove leading slashes
print(final_path)  # Output the final processed path
