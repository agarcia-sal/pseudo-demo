import os

def normalize_file_path(input_string):
    # Normalize the file path by resolving relative components
    return os.path.normpath(input_string)

def clean_file_path(normalized_path):
    # Clean the path by replacing leading forward slashes with a single slash
    return normalized_path.lstrip('/').rstrip('/')

# Start Program
# Get Input
input_string = input().strip()

# Normalize Path
normalized_path = normalize_file_path(input_string)

# Clean Path
cleaned_path = clean_file_path(normalized_path)

# Output Result
print(f"/{cleaned_path}")
# End Program
