# Start the process

# Read Input
file_path = input().strip()  # Obtain the input and remove leading/trailing spaces

# Normalize the File Path
if file_path.startswith('/'):
    # Replace any sequence of slashes at the beginning with a single slash
    while file_path.startswith('//'):
        file_path = file_path[1:]  # Remove an extra leading slash
    file_path = '/' + file_path.lstrip('/')  # Ensure it's a single leading slash

# Output the Result
print(file_path)  # Display the modified file path

# End the process
