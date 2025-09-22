import os

def normalize_path(input_string):
    # Normalize the input string to an absolute path form
    return os.path.normpath(input_string)

def clean_path(normalized_path):
    # Clean the path by replacing leading slashes with a single slash
    if normalized_path.startswith('/'):
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path
    return cleaned_path

def main():
    # Get input from the user
    input_string = input().strip()  # Read input and remove any leading/trailing whitespace

    # Normalize and clean the path
    normalized_path = normalize_path(input_string)
    cleaned_path = clean_path(normalized_path)

    # Output the final cleaned path
    print(cleaned_path)

# Start the program
if __name__ == "__main__":
    main()
