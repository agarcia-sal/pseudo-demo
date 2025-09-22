def normalize_path(input_path):
    # Normalize the input path by removing redundant separators
    parts = input_path.split('/')  # Split the path by '/'
    # Filter out empty parts caused by multiple consecutive slashes
    filtered_parts = [part for part in parts if part]  
    normalized_path = '/'.join(filtered_parts)  # Join the parts back with '/'
    return normalized_path

# Start of the main program
file_path = input()  # Read entire file path input

# Normalize the file path
normalized_path = normalize_path(file_path)

# Ensure that the normalized path starts with a single forward slash
if normalized_path.startswith('//'):
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace multiple slashes with a single slash

# Output the final normalized path
print(normalized_path)
