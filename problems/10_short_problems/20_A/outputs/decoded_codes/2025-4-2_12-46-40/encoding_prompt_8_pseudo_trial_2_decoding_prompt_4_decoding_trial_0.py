def normalize_path(input_path: str) -> str:
    """
    Normalize the input path by removing redundant separators
    and resolving any up-level references.
    """
    # Split the path into components, removing empty components
    components = input_path.split('/')
    normalized_components = []

    for part in components:
        if part == '' or part == '.':
            # Ignore empty parts and current directory references
            continue
        elif part == '..':
            # Move up one level if possible
            if normalized_components:
                normalized_components.pop()
        else:
            normalized_components.append(part)

    # Join the normalized components back into a path
    normalized_input_path = '/'.join(normalized_components)
    return normalized_input_path


def replace_multiple_leading_slashes(path: str) -> str:
    """
    Ensure the normalized path starts with a single '/'.
    Replace any occurrence of multiple leading slashes with a single slash.
    """
    if path.startswith('/'):
        # Replace multiple leading slashes with a single '/'
        path = '/' + path.lstrip('/')
    else:
        path = '/' + path  # Prepend a single slash if none exists
    
    return path


# Step 1: Read the input file path from standard input
user_input = input()

# Step 2: Normalize the input path
normalized_path = normalize_path(user_input)

# Step 3: Ensure the normalized path starts with a single '/'
final_path = replace_multiple_leading_slashes(normalized_path)

# Step 4: Print the final normalized path
print(final_path)
