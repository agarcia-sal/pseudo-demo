def normalize_file_path():
    # Read the input directly from the user
    input_path = get_user_input()
    
    # Clean up the input by removing unnecessary spaces and normalizing slashes
    cleaned_path = normalize_path(input_path)
    
    # Ensure that the cleaned path starts with a single forward slash
    final_path = replace_multiple_leading_slashes_with_single(cleaned_path)
    
    # Output the final normalized path
    print(final_path)

def get_user_input():
    # Read the input, strip away any leading or trailing whitespace
    return input().strip()

def normalize_path(path):
    # Normalize slashes and resolve any redundant navigation symbols
    # Replace backslashes with forward slashes
    normalized_path = path.replace('\\', '/')
    
    # Split the path into parts and filter out '.' and empty strings
    parts = normalized_path.split('/')
    filtered_parts = [part for part in parts if part and part != '.']
    
    # Resolve '..' by removing the last added directory when possible
    final_parts = []
    for part in filtered_parts:
        if part == '..':
            if final_parts:  # Only pop if there are directories to pop
                final_parts.pop()
        else:
            final_parts.append(part)

    # Join back the cleaned parts with a single slash
    return '/'.join(final_parts)

def replace_multiple_leading_slashes_with_single(path):
    # Check if the path starts with one or more slashes
    if path.startswith('/'):
        # Remove all leading slashes except one
        return '/' + path.lstrip('/')
    return path

# Begin execution
normalize_file_path()
