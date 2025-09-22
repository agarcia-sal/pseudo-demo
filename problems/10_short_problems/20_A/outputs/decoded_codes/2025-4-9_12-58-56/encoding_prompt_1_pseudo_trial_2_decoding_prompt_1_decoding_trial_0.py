# Start the Program

# Define a Function to Normalize File Paths
def normalize_file_path(file_path):
    # Normalize the File Path
    # Change the file path to a standard format
    # Replace any backslashes with forward slashes
    normalized_path = file_path.replace('\\', '/')
    
    # Eliminate redundant slashes within the path
    while '//' in normalized_path:
        normalized_path = normalized_path.replace('//', '/')

    # Adjust Leading Slashes
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')  # Keep only one leading slash

    return normalized_path

# Read Input
file_path = input().strip()  # Read the file path and remove extra spaces

# Normalize the File Path
normalized_path = normalize_file_path(file_path)

# Display the Normalized Path
print(normalized_path)

# End the Program
