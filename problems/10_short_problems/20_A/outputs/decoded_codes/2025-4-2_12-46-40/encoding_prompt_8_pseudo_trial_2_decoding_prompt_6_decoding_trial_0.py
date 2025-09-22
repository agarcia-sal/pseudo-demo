# Function to normalize the input file path
def normalize_path(input_path):
    # Placeholder for normalization logic
    # In a real implementation, this would remove redundant segments
    normalized_input_path = input_path  # For simplicity, just returning the input
    return normalized_input_path

# Function to replace multiple leading slashes with a single slash
def replace_multiple_leading_slashes(path):
    if path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        while path.startswith('//'):
            path = path.replace('//', '/')
        return path
    else:
        # Prepend a single slash if none exists
        return '/' + path

# Step 1: Read the input file path from standard input
user_input = input()

# Step 2: Normalize the input path
normalized_path = normalize_path(user_input)

# Step 3: Ensure the normalized path starts with a single '/' 
final_path = replace_multiple_leading_slashes(normalized_path)

# Step 4: Print the final normalized path
print(final_path)
