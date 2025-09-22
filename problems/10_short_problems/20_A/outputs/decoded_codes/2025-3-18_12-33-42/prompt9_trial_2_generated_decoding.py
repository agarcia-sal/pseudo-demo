def normalize_path(path):
    # Normalize the path by removing redundant separators
    path_parts = path.split("/")  # Split the path into parts
    # Filter out empty parts to remove redundant slashes
    filtered_parts = [part for part in path_parts if part]
    normalized_path = "/".join(filtered_parts)  # Join parts with a single slash
    return normalized_path

# Step 1: Receive Input
input_path = input().strip()  # Read a file path and remove whitespace

# Step 2: Normalize the Path
normalized_path = normalize_path(input_path)

# Step 3: Replace Leading Slashes
if normalized_path.startswith("/"): 
    # Ensure only a single leading slash
    normalized_path = "/" + normalized_path.lstrip("/")  # Remove excess leading slashes

# Step 4: Display the Result
print(normalized_path)  # Print the updated file path
