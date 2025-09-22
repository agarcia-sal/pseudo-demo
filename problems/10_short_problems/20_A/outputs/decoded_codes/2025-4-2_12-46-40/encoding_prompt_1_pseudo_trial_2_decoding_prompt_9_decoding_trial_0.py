import os

def normalize_path(input_string):
    # Normalize the path to resolve any relative components
    return os.path.normpath(input_string)

def clean_path(normalized_path):
    # Clean the path to replace leading slashes with a single forward slash
    return '/' + normalized_path.lstrip('/')

# Start Program
input_string = input().strip()  # Read input and remove leading/trailing whitespace

normalized_path = normalize_path(input_string)  # Normalize the input path
cleaned_path = clean_path(normalized_path)  # Clean the normalized path

print(cleaned_path)  # Output the final cleaned path
# End Program
