# Step 1: Import necessary libraries
import os

# Step 2: Read the entire input from standard input
file_path_input = input().strip()  # Removing leading/trailing whitespace

# Step 4: Normalize the file path
# a. Transforming backslashes to forward slashes
normalized_path = file_path_input.replace("\\", "/")

# Step 5: Process the normalized file path
# a. Ensure it starts with a single forward slash
if normalized_path.startswith("//"):
    normalized_path = "/" + normalized_path.lstrip("/")
elif not normalized_path.startswith("/"):
    normalized_path = "/" + normalized_path

# Step 6: Output the final processed file path
print(normalized_path)
