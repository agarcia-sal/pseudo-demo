import os
import re

def normalize(path):
    # Normalize the file path using os.path.normpath
    return os.path.normpath(path)

def remove_leading_slashes(path):
    # Use regex to ensure at most one leading slash
    clean_path = re.sub(r'^/+','', path)  # Remove all leading slashes
    return '/' + clean_path if clean_path else ''

# Main execution block
input_string = input()
normalized_path = normalize(input_string)
final_path = remove_leading_slashes(normalized_path)

print(final_path)
