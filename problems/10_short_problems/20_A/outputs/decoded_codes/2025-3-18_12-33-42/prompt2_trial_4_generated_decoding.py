# Step 1: Input Requirement
file_path = input()

# Step 2: Process the Input
# Normalize the file path by removing unnecessary components
# Here we can use the str.replace() method to simplify the process

# Step 3: Clean the File Path
# Ensure that the normalized file path does not start with multiple forward slashes
# We replace occurrences of '//' with '/', then take care of multiple leading slashes

# Normalize the path by replacing multiple slashes with a single one first
normalized_path = file_path.replace('//', '/')

# Then we check for leading slashes
while normalized_path.startswith('//'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 4: Output the Result
print(normalized_path)
