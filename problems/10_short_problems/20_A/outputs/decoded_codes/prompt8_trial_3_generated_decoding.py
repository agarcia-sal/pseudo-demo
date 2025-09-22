def normalize(path):
    # Replace multiple slashes with a single slash and remove current directory (.)
    normalized_path = '/'.join(part for part in path.split('/') if part not in ('', '.'))
    return normalized_path

# Step 1: Get user input
inputPath = input()

# Step 2: Normalize the input path
normalizedPath = normalize(inputPath)

# Step 3: Ensure only one leading slash
if normalizedPath.startswith('/'):
    normalizedPath = '/' + normalizedPath.lstrip('/')
else:
    normalizedPath = '/' + normalizedPath

# Step 4: Display the final cleaned path
print(normalizedPath)
