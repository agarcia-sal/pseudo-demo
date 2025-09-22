def normalize_path(input_path):
    # Split the input path by slashes and filter out empty sections
    parts = input_path.split('/')
    normalized_parts = [part for part in parts if part]  # Remove empty sections
    # Join the filtered parts with a single slash
    normalized_path = '/' + '/'.join(normalized_parts) if normalized_parts else '/'
    return normalized_path


# Step 1: Read entire file path input
file_path = input()

# Step 2: Normalize the file path
normalized_path = normalize_path(file_path)

# Step 3: Ensure that the normalized path starts with a single forward slash
if normalized_path.startswith('//'):
    normalized_path = normalized_path.replace('//', '/')

# Step 4: Output the final normalized path
print(normalized_path)
