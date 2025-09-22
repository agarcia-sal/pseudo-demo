import os

# Step 1: Read the input file path
raw_file_path = input().strip()  # Trim spaces from the beginning and end

# Step 2: Normalize the file path
normalized_path = os.path.normpath(raw_file_path)  # Use standard normalization method

# Step 3: Remove leading slashes
if normalized_path.startswith('/'):
    cleaned_path = '/' + normalized_path.lstrip('/')  # Replace leading slashes with a single slash
else:
    cleaned_path = normalized_path  # No leading slashes to remove

# Step 4: Display the cleaned file path
print(cleaned_path)
