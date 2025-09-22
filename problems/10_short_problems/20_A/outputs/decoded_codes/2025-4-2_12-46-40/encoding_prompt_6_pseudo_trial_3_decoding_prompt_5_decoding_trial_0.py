import os

def process_file_path():
    # Read input from standard input and remove any leading/trailing whitespace
    input_string = input()
    trimmed_input_string = input_string.strip()

    # Normalize the path, converting it to a standard format
    normalized_path = os.path.normpath(trimmed_input_string)

    # Replace any sequence of leading slashes with a single slash
    if normalized_path.startswith('/'):
        updated_path = '/' + normalized_path.lstrip('/')
    else:
        updated_path = normalized_path.lstrip('/')

    # Output the final transformed path
    print(updated_path)

# Example test cases (uncomment to use)
# This will not be executed in this context but can be used for testing
# Assume the input is the file path entered by the user.
# process_file_path()
