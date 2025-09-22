# Step 1: Input
path = input().strip()  # Read the input and remove surrounding spaces

# Step 2: Normalize the path (handled by stripping spaces in this case)
normalized_path = path  # For this specific case, just use the stripped path

# Step 3: Handle multiple leading forward slashes
if normalized_path.startswith("//"):  # Check for multiple leading slashes
    # Replace leading slashes with a single slash
    while normalized_path.startswith("/"):
        normalized_path = normalized_path[1:]  # Remove the leading slash
    normalized_path = "/" + normalized_path  # Add back a single leading slash

# Step 4: Output the cleaned-up path
print(normalized_path)
