import os

def normalize_file_path(file_path):
    # Remove extra whitespace
    cleaned_path = file_path.strip()

    # Normalize the file path using os.path.normpath
    normalized_path = os.path.normpath(cleaned_path)

    # Adjust leading slashes to ensure only one leading slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]

    # Ensure it starts with a single slash
    final_path = '/' + normalized_path

    return final_path

# Start of Program
if __name__ == "__main__":
    input_path = input()
    result = normalize_file_path(input_path)
    print(result)
