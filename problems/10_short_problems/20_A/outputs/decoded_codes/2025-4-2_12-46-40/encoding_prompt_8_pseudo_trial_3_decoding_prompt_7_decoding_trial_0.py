def normalize_path(path):
    # Split the path into components and filter out unnecessary components
    parts = path.split('/')
    normalized_parts = []
    
    for part in parts:
        if part == '' or part == '.':
            # Skip empty parts and current directory references
            continue
        elif part == '..':
            # Handle the up-level directory reference
            if normalized_parts:
                normalized_parts.pop()  # Go back one directory
        else:
            normalized_parts.append(part)  # Add valid part to normalized list

    # Join the parts to form the normalized path
    normalized_path = '/'.join(normalized_parts)
    return normalized_path

# Step 1: Read input
original_path = input()
# Remove extra whitespace from both ends of input
trimmed_path = original_path.strip()

# Step 2: Normalize the file path
normalized_path = normalize_path(trimmed_path)

# Step 3: Ensure the path starts with a single forward slash
if not normalized_path.startswith('/'):
    final_path = '/' + normalized_path
else:
    final_path = '/' + normalized_path.lstrip('/')  # Remove excess slashes but keep one

# Step 4: Output the final result
print(final_path)
