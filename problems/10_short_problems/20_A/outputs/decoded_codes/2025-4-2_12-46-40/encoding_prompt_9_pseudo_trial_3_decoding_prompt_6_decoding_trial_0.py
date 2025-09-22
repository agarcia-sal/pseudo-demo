# Step 1: Read the entire input from standard input and strip any extra whitespace
file_path = input().strip()

# Step 2: Normalize the file path by splitting and filtering unnecessary path elements
# We'll use the split method and join method to achieve a normalized path
normalized_path = '/'.join(filter(None, file_path.split('/')))

# Step 3: Ensure the normalized path starts with a single root slash
if normalized_path.startswith('/'):
    final_path = '/' + normalized_path.lstrip('/')
else:
    final_path = '/' + normalized_path

# Step 4: Output the final path
print(final_path)
