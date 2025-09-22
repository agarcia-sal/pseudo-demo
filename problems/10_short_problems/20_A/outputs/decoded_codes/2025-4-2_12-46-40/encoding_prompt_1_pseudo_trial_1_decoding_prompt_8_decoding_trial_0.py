import os

def normalize_file_path(file_path):
    # Remove extra whitespace
    file_path = file_path.strip()
    # Normalize the file path
    normalized_path = os.path.normpath(file_path)
    # Adjust leading slashes
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    return normalized_path

# Start of Program
file_path_input = input()
result = normalize_file_path(file_path_input)
print(result)
# End of Program
