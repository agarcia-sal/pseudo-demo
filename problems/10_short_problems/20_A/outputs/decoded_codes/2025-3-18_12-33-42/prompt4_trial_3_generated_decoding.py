import os

def normalize_path(input_path):
    # Normalize the input path using os.path.normpath to remove redundant separators
    # and up-level references
    normalized_path = os.path.normpath(input_path)
    
    # Check for leading slashes and replace them with a single slash
    if normalized_path.startswith('/'):
        final_path = '/' + normalized_path.lstrip('/')
    else:
        final_path = normalized_path

    return final_path

# Read input path from standard input
input_path = input()

# Normalize the path
final_path = normalize_path(input_path)

# Output the final cleaned path
print(final_path)
