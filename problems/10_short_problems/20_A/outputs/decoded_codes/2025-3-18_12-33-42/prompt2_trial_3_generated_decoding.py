# Begin Program

# Input
file_path = input().strip()  # Read a line of text and remove leading and trailing spaces

# Process
# Step 1: Normalize the file path
# Replace multiple consecutive slashes with a single slash
normalized_path = '/' + '/'.join(part for part in file_path.split('/') if part)  # Join non-empty parts with a single slash

# Step 2: Clean the beginning of the path
if normalized_path.startswith('//'):
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace leading slashes with a single slash

# Output
print(normalized_path)  # Print the cleaned and normalized file path

# End Program
