# Start the process

# Read Input
file_path = input()  # Obtain a string input representing a file path
file_path = file_path.strip()  # Remove leading and trailing spaces

# Normalize the File Path
if file_path.startswith('/'):
    file_path = '/' + file_path.lstrip('/')  # Ensure only one leading slash

# Output the Result
print(file_path)  # Display the modified file path

# End the process
