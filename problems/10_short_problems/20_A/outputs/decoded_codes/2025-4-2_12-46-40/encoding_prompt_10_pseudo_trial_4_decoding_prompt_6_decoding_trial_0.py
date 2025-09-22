import re

def read_from_standard_input():
    # Read input from standard input
    return input()

def normalize_path(path):
    # Normalize the path to a standard format
    # Here we make sure to convert backslashes to slashes for POSIX compatibility
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    # Replace one or more leading slashes with a single slash
    return re.sub(r'^/+', '/', path)

def main():
    # Step 1: Read input from system standard input
    input_string = read_from_standard_input()

    # Step 2: Normalize the path
    normalized_path = normalize_path(input_string)

    # Step 3: Remove leading slashes from the normalized path
    cleaned_path = remove_leading_slashes(normalized_path)

    # Step 4: Print the cleaned path
    print(cleaned_path)

# Run the main function
main()
