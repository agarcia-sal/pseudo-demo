# Start Program

# Step 1: Read entire file path input
filePath = input()

# Step 2: Normalize the file path
def normalize_path(inputPath):
    # Replaces multiple slashes and resolves redundant sections
    normalizedPath = inputPath.replace('//', '/')  # Simplified version for demonstration
    while '//' in normalizedPath:
        normalizedPath = normalizedPath.replace('//', '/')
    normalizedPath = normalizedPath.strip('/')  # Remove leading and trailing slashes for clean processing
    return normalizedPath

normalizedPath = normalize_path(filePath)

# Step 3: Ensure that the normalized path starts with a single forward slash
if normalizedPath.startswith('//'):
    normalizedPath = '/' + normalizedPath.lstrip('/')

# Step 4: Output the final normalized path
print(normalizedPath)

# End Program
