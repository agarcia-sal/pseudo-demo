import os

def main():
    # Read input path from standard input
    input_path = input()

    # Normalize the input path using POSIX standards
    normalized_path = os.path.normpath(input_path)

    # Remove leading slashes, ensuring at least one leading slash remains
    result_path = normalize_leading_slashes(normalized_path)

    # Output the final processed path
    print(result_path)

def normalize_leading_slashes(path):
    if path.startswith('/'):
        # Replace all leading slashes with a single slash
        path = '/' + path.lstrip('/')
    return path

if __name__ == "__main__":
    main()
