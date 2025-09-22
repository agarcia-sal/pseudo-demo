import re

def process_input_path():
    # Read input path from standard input and remove leading/trailing whitespace
    input_path = input().strip()
    
    # Normalize the path to ensure consistent formatting
    normalized_path = normalize_path(input_path)
    
    # Remove any leading slashes from the normalized path and ensure a single leading slash
    final_path = remove_leading_slashes(normalized_path)
    
    # Print the final processed path
    print(final_path)

def normalize_path(path):
    # Normalize the input path to a standard format using forward slashes
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    # Use regular expression to replace multiple leading slashes with a single slash
    return re.sub(r'^/+','/', path)

# If this file is being run directly, execute the path processing
if __name__ == "__main__":
    process_input_path()
