def normalize_path(input_path):
    # This function transforms the file path to a standard format
    # Implementation details of normalization can depend on specific requirements
    # As an example, we could make the path lowercase for normalization
    normalized_path = input_path.lower()  # Example normalization step
    return normalized_path

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Ensure there's a single leading slash

# BEGIN PROGRAM

# Read input from standard input and remove extra spaces
input_path = input().strip()

# Normalize the file path
normalized_path = normalize_path(input_path)

# Replace any sequence of leading slashes with a single slash
final_path = replace_leading_slashes(normalized_path)

# Output the final normalized path
print(final_path)

# END PROGRAM
