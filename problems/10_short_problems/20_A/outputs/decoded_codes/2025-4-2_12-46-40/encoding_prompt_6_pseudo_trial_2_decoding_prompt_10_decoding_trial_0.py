def read_input():
    # Read input from standard input and remove extra spaces
    input_path = input().strip()
    return input_path

def normalize_path(input_path):
    # This function transforms the file path to a standard format.
    # Assuming normalization means removing redundant components
    # Here we will perform a simple normalization using os.path.abspath
    import os
    normalized_path = os.path.normpath(input_path)
    return normalized_path

def replace_leading_slashes(path):
    # This function replaces sequences of leading slashes at the start of the path
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return '/' + path  # Add a single leading slash

def main():
    # Main execution flow of the program
    input_path = read_input()
    normalized_path = normalize_path(input_path)
    final_path = replace_leading_slashes(normalized_path)

    # Output the final normalized path
    print(final_path)

if __name__ == "__main__":
    main()
