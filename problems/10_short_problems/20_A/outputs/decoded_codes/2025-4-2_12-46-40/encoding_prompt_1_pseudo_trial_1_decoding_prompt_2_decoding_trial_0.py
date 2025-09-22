import os

# Start of Program

# Step 2: Read Input
file_path = input()

# Step 3: Remove Extra Whitespace
file_path = file_path.strip()

# Step 4: Normalize the File Path
normalized_path = os.path.normpath(file_path)

# Step 5: Adjust Leading Slashes
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 6: Output the Result
print(normalized_path)

# End of Program
