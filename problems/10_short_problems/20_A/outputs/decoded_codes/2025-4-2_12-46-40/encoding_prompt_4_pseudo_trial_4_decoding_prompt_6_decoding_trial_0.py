# Read a file path input from standard input
input_path = input()

# Normalize the file path by removing redundant separators
normalized_path = '/'.join(part for part in input_path.split('/') if part)

# Replace any leading slashes with a single leading slash
cleaned_path = '/' + normalized_path.lstrip('/')

# Output the cleaned path
print(cleaned_path)
