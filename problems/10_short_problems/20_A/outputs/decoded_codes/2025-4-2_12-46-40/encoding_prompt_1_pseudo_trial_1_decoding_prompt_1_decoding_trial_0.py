# Start of Program

# Read Input
file_path = input()

# Remove Extra Whitespace
file_path = file_path.strip()

# Normalize the File Path
import os
normalized_path = os.path.normpath(file_path)

# Adjust Leading Slashes
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Output the Result
print(normalized_path)

# End of Program
