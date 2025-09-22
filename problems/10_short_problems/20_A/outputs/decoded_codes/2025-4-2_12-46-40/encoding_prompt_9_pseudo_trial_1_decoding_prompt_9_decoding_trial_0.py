import os

# Start Program

# Receive Input
raw_path = input().strip()  # Read input data and remove extra spaces

# Normalize Path
# Use os.path.normpath to clean up the path, resolving ".." and "."
normalized_path = os.path.normpath(raw_path)

# Ensure Single Leading Slash
if normalized_path.startswith("//"):  # Check for multiple leading slashes
    normalized_path = "/" + normalized_path.lstrip("/")  # Replace with a single leading slash

# Output Result
print(normalized_path)  # Print the final normalized path

# End Program
