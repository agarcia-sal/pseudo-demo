# Start Program

# Receive Input
input_data = input().strip()  # Read input and remove any leading/trailing whitespace

# Normalize Path
# Using the os.path library to clean up the path
import os
normalized_path = os.path.normpath(input_data)  # Normalize the path

# Ensure Single Leading Slash
if normalized_path.startswith('//'):  # Check if the path starts with multiple slashes
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace with a single leading slash

# Output Result
print(normalized_path)  # Print the final normalized path

# End Program
