# Start Program

# Receive Input:
path = input().strip()  # Read input data and remove any extra spaces from both ends

# Normalize Path:
import os
normalized_path = os.path.normpath(path)  # Normalize the path

# Ensure Single Leading Slash:
if normalized_path.startswith("//"):  # Check if the normalized path starts with multiple slashes
    normalized_path = "/" + normalized_path.lstrip("/")  # Replace with a single slash

# Output Result:
print(normalized_path)  # Print the final normalized path

# End Program
