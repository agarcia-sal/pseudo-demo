def normalize_path(inputPath):
    # Split the path by '/' and filter out empty sections
    parts = inputPath.split('/')
    # Remove redundant sections (i.e., '.', '..', and empty parts)
    normalized_parts = []
    for part in parts:
        if part in ['.', '']:  # Ignore current directory and empty parts
            continue
        if part == '..':
            if normalized_parts:
                normalized_parts.pop()  # Remove the last valid part for parent directory
        else:
            normalized_parts.append(part)
    
    # Join the normalized path with a single '/'
    normalizedPath = '/'.join(normalized_parts)
    
    return normalizedPath

# Start Program
filePath = input()

# Normalize Path
normalizedPath = normalize_path(filePath)

# Ensure Leading Slash
if normalizedPath.startswith('//'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# Output Result
print(normalizedPath)
