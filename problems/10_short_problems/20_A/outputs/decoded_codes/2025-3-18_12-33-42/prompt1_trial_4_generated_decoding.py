# Start the program
# Read input from the standard input
file_path = input()

# Remove any leading and trailing whitespace from the input
file_path = file_path.strip()

# Normalize the file path
# Replace any sequences of forward slashes ("/") at the beginning of the path with a single forward slash ("/")
if file_path.startswith('/'):
    file_path = '/' + file_path.lstrip('/')

# Print the normalized file path
print(file_path)

# End of the program
