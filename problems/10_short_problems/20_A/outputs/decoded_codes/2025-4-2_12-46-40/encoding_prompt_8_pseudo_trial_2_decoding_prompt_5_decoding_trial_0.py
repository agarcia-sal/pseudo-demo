def normalize_path(input_path):
    # Split the input path into segments separated by slashes
    path_segments = input_path.split('/')
    # Filter out empty segments and redundant elements
    cleaned_segments = [segment for segment in path_segments if segment]
    # Return the normalized path by joining the cleaned segments with a single slash
    return '/'.join(cleaned_segments)

def replace_multiple_leading_slashes(path):
    # Check for the leading slashes in the path
    if path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        return '/' + path.lstrip('/')
    else:
        # Prepend a single slash if no leading slash exists
        return '/' + path

# Step 1: Read the input file path from standard input
user_input = input()

# Step 2: Normalize the input path
normalized_path = normalize_path(user_input)

# Step 3: Ensure the normalized path starts with a single '/'
final_path = replace_multiple_leading_slashes(normalized_path)

# Step 4: Print the final normalized path
print(final_path)
