# Start the program
# Read input from the standard input source
input_path = input()

# Remove unnecessary leading whitespace from the input
cleaned_path = input_path.strip()

# Normalize the file path
if cleaned_path.startswith('/'):
    # Replace multiple leading slashes with a single slash
    cleaned_path = '/' + cleaned_path.lstrip('/')

# Output the normalized file path
print(cleaned_path)
