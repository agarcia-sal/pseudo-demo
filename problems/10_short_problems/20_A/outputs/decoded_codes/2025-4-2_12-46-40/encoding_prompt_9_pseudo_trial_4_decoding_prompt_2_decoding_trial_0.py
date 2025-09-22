def normalize_path(input_path):
    # Split the input path by slashes and filter out redundant parts
    parts = input_path.split('/')
    normalized_parts = [part for part in parts if part]
    # Join them back together with a single slash
    normalized_path = '/' + '/'.join(normalized_parts)
    return normalized_path

# Start Program
filePath = input()  # Step 1: Read entire file path input
normalizedPath = normalize_path(filePath)  # Step 2: Normalize the file path

# Step 3: Ensure that the normalized path starts with a single forward slash
if normalizedPath.startswith('//'):
    normalizedPath = '/' + normalizedPath.lstrip('/')  # Replace multiple slashes at the start with a single slash

# Step 4: Output the final normalized path
print(normalizedPath)  # Output the final normalized path
