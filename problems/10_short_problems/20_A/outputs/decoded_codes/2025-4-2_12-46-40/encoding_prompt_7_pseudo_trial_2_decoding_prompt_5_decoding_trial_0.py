import re

def process_input_path():
    # Read input from standard input and remove leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the path to ensure consistent formatting
    normalized_path = normalize_path(input_path)
    
    # Remove any leading slashes and ensure a single leading slash
    final_path = remove_leading_slashes(normalized_path)
    
    # Print the final processed path
    print(final_path)

def normalize_path(path):
    # Normalize the input path to a standard format using forward slashes
    return path.replace('\\', '/')  # Replace backslashes with forward slashes

def remove_leading_slashes(path):
    # Use regular expression to replace multiple leading slashes with a single slash
    return re.sub(r'^/+','/', path)  # Replace multiple leading slashes with a single one

# Testing the functions
# Consider testing with different paths such as:
# process_input_path()  # Input: "///foo/bar" should output: "/foo/bar"
# process_input_path()  # Input: "\\foo\\bar\\" should output: "/foo/bar/"
# process_input_path()  # Input: "" should output: "/"
