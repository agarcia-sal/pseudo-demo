# Step 1: Read input
original_path = input()  # Obtain the entire text input from standard input
trimmed_path = original_path.strip()  # Remove extra whitespace from both ends of original_path

# Step 2: Normalize the file path
# Split the path by the separator '/' and filter out any empty segments or '.' entries
path_segments = [segment for segment in trimmed_path.split('/') if segment and segment != '.']
normalized_path = '/'.join(path_segments)  # Join the cleaned segments back into a path

# Step 3: Ensure the path starts with a single forward slash
if normalized_path:  # Check if normalized_path is not empty
    final_path = '/' + normalized_path.lstrip('/')  # Add a leading slash if necessary and remove extra slashes
else:
    final_path = '/'  # If empty, ensure at least one leading slash

# Step 4: Output the final result
print(final_path)  # Print the adjusted path to the standard output
