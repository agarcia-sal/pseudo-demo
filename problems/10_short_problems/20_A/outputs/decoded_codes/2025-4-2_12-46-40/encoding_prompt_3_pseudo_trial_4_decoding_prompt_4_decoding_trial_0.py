def normalize_path(path):
    # Convert backslashes to forward slashes and remove unnecessary segments
    path = path.replace('\\', '/')
    segments = path.split('/')
    
    # Use a stack to handle the path segments
    stack = []
    for segment in segments:
        if segment == '' or segment == '.':
            # Skip empty segments and current directory indicators
            continue
        elif segment == '..':
            # Pop the last segment if it exists (going up one directory)
            if stack:
                stack.pop()
        else:
            # Add the segment to the stack
            stack.append(segment)

    # Join the segments back together into a normalized path
    normalized = '/'.join(stack)
    return normalized

def remove_leading_slashes(path):
    # If the path starts with one or more slashes, replace it with a single slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    return path

# Read input from the standard input
input_string = input()

# Normalize the path
normalized_path = normalize_path(input_string)

# Remove leading slashes
final_path = remove_leading_slashes(normalized_path)

# Output the final processed path
print(final_path)
