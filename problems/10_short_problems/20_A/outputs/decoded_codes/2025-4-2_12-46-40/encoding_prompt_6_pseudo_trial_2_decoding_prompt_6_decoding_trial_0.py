def normalize_path(input_path):
    # This function transforms the file path to a standard format
    # Placeholder implementation; replace with actual normalization logic as needed
    return input_path.strip()  # Example: Currently just trimming whitespace

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):  # While the path starts with a slash
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash back

# Read input from standard input and remove extra spaces
input_path = input().strip()  # Read input and strip leading/trailing whitespace

# Normalize the file path
normalized_path = normalize_path(input_path)

# Replace any sequence of leading slashes with a single slash
final_path = replace_leading_slashes(normalized_path)

# Output the final normalized path
print(final_path)
