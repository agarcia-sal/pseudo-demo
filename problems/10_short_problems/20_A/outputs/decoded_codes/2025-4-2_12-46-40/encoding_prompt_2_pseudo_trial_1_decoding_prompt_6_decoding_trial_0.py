# Start the process.

# Step 2: Read Input
# Obtain a string input representing a file path and trim leading/trailing spaces
file_path = input().strip()

# Step 3: Normalize the File Path
# Replace any sequence of slashes at the beginning of the path with a single slash
if file_path.startswith('/'):
    # Remove existing leading slashes and replace with a single leading slash
    normalized_path = '/' + file_path.lstrip('/')
else:
    # If no leading slash is present, just return the file path as is
    normalized_path = file_path

# Step 4: Output the Result
# Display the modified file path
print(normalized_path)

# End the process.
