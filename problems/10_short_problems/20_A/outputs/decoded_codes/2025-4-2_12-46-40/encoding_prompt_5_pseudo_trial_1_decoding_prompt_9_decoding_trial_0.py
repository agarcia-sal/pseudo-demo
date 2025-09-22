def read_input():
    # Get the path from standard input and remove excess whitespace
    input_path = input().strip()
    return input_path

def normalize_path(path):
    # Normalize the file path to remove any redundant separators and up-level references
    normalized_path = remove_reductions_from_path(path)
    return normalized_path

def remove_reductions_from_path(path):
    # This function removes redundant slashes and handles up-level references
    # For simplicity, we split the path and then rejoin without extra slashes
    parts = path.split('/')
    cleaned_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            continue  # Skip empty parts and current directory references
        if part == '..':
            if cleaned_parts:
                cleaned_parts.pop()  # Remove the last part for up-level references
        else:
            cleaned_parts.append(part)

    return '/' + '/'.join(cleaned_parts)  # Join the cleaned parts back with a leading slash

def ensure_single_leading_slash(path):
    # If the path starts with one or more slashes 
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        adjusted_path = '/'.join(path.split('/')[1:])  # Remove leading slashes
        return '/' + adjusted_path
    else:
        return path  # Return the path as is since it already has a single slash

def main():
    # Read and clean the input path
    user_input = read_input()
    
    # Normalize the input path for standardization
    normalized_input = normalize_path(user_input)
    
    # Ensure the normalized path has a proper leading slash
    final_path = ensure_single_leading_slash(normalized_input)
    
    # Output the final cleaned path
    print(final_path)

main()
