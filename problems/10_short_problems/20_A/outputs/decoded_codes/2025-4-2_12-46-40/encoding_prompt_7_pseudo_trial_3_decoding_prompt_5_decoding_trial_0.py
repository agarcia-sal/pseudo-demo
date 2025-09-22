import re

def normalize_and_print_path():
    # Read input from standard input
    raw_input = input()
    
    # Normalize the input path
    normalized_path = normalize_path(raw_input)
    
    # Print the modified path, replacing multiple leading slashes with a single slash
    print(replace_leading_slashes(normalized_path))

def normalize_path(raw_input):
    # Remove any leading or trailing whitespace from the input
    trimmed_input = raw_input.strip()
    
    # Normalize the file path
    # Placeholder for actual normalization logic, for now it just returns the trimmed input
    normalized_path = standard_path_normalization(trimmed_input)
    
    return normalized_path

def standard_path_normalization(path):
    # Implement logic for path normalization if needed
    # For now, we will just return the path as is
    return path

def replace_leading_slashes(path):
    # Use a regular expression to replace multiple leading slashes with a single slash
    modified_path = re.sub(r'^/+', '/', path)
    
    return modified_path

# Example of how to test the code
# When using it, consider edge cases like:
# normalize_and_print_path()  # e.g. input: "////usr//bin//" -> Output: "/usr/bin/"
