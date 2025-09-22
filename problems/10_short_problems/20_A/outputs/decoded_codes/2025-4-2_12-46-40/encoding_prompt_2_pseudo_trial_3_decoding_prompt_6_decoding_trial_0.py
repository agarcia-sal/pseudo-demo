# Step 1: Read a string input representing a file path
file_path = input().strip()  # Remove any extra spaces

# Step 2: Normalize the input path
normalized_path = file_path.replace("\\", "/")  # Replace backslashes with forward slashes

# Step 3: Check for leading slashes
if normalized_path.startswith("/"):  # Check if the path starts with a forward slash
    while normalized_path.startswith("//"):  # While there are multiple leading slashes
        normalized_path = normalized_path[1:]  # Remove one leading slash

# Ensure that it starts with exactly one forward slash
if not normalized_path.startswith("/"):
    normalized_path = "/" + normalized_path  # Add a single forward slash at the start if missing

# Step 4: Print the cleaned-up file path
print(normalized_path)
