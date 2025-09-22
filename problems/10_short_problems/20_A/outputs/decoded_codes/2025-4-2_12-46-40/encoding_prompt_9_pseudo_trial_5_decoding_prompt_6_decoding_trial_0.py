# Step 1: Read Input
file_path = input()  # Obtain the file path from the user

# Step 2: Normalize the File Path
# We will replace multiple slashes with a single slash
normalized_path = "/".join(segment for segment in file_path.split("/") if segment)

# Step 3: Remove Leading Slashes
# Ensure that the final path starts with a single slash
if normalized_path.startswith("/"):
    final_path = "/" + normalized_path.lstrip("/")
else:
    final_path = normalized_path

# Step 4: Output the Final Path
print(final_path)  # Display the cleaned file path
