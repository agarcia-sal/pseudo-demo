def normalize_path(input_path):
    # Normalize the path by splitting it and filtering out empty segments
    # This removes any redundant separators (e.g., '///' to '/') and '.' while resolving '..'
    segments = input_path.split('/')
    filtered_segments = []
    
    for segment in segments:
        if segment == '' or segment == '.':
            # Skip empty segments (redundant slashes) and current directory indicators
            continue
        elif segment == '..':
            # Pop the last valid segment if the segment is '..' unless we are at the root level
            if filtered_segments:
                filtered_segments.pop()
        else:
            # Add valid segment to the list
            filtered_segments.append(segment)

    # Join the filtered segments back into a normalized path
    normalized_path = '/' + '/'.join(filtered_segments)
    return normalized_path

# Step 1: Read entire file path input
file_path = input()

# Step 2: Normalize the file path
normalized_path = normalize_path(file_path)

# Step 3: Ensure that the normalized path starts with a single forward slash
while normalized_path.startswith('//'):
    normalized_path = normalized_path.replace('//', '/', 1)

# Step 4: Output the final normalized path
print(normalized_path)
