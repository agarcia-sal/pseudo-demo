def normalize_path(input_path):
    # This function should contain logic to normalize the path
    # For simplicity's sake, assuming it removes redundant elements
    parts = input_path.split('/')
    normalized_parts = []
    
    for part in parts:
        if part and part != '.':
            if part == '..':
                if normalized_parts:
                    normalized_parts.pop()
            else:
                normalized_parts.append(part)
    
    normalized_input_path = '/'.join(normalized_parts)
    return normalized_input_path

def replace_multiple_leading_slashes(path):
    # Check for slashes at the start of the path and replace them accordingly
    if path.startswith('/'):
        return '/' + path.lstrip('/').replace('//', '/')
    else:
        return '/' + path

# Step 1: Read the input file path from standard input
user_input = input()

# Step 2: Normalize the input path
normalized_path = normalize_path(user_input)

# Step 3: Ensure the normalized path starts with a single '/'
final_path = replace_multiple_leading_slashes(normalized_path)

# Step 4: Print the final normalized path
print(final_path)
