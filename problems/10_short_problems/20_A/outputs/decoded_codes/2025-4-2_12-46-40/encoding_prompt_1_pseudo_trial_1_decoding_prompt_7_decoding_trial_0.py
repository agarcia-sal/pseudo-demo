import os

def normalize_file_path(file_path):
    # Normalize the file path using os.path.normpath to handle redundant separators and up-level references
    normalized_path = os.path.normpath(file_path)
    return normalized_path

# Start of Program
# Step 2: Read Input
input_path = input()  # Read a string from standard input representing a file path

# Step 3: Remove Extra Whitespace
trimmed_path = input_path.strip()  # Trim whitespace from the beginning and end

# Step 4: Normalize the File Path
normalized_path = normalize_file_path(trimmed_path)

# Step 5: Adjust Leading Slashes
if normalized_path.startswith('/'):
    # If the path starts with one or more slashes, replace all leading slashes with a single slash
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 6: Output the Result
print(normalized_path)  # Print the final adjusted file path
