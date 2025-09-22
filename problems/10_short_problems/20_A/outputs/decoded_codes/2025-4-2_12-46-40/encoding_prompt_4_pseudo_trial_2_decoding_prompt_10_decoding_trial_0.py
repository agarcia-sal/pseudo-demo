import os

def normalize_and_format_path():
    # Read input from standard input and remove extra whitespace
    input_path = input().strip()
    
    # Normalize the file path by collapsing redundant separators
    normalized_path = os.path.normpath(input_path)
    
    # Replace any leading slashes with a single slash
    if normalized_path.startswith('/'):
        formatted_path = '/' + normalized_path.lstrip('/')
    else:
        formatted_path = normalized_path

    # Output the formatted path
    print(formatted_path)

# This allows the function to be called only when the script is run directly,
# preventing it from executing on import.
if __name__ == "__main__":
    normalize_and_format_path()
