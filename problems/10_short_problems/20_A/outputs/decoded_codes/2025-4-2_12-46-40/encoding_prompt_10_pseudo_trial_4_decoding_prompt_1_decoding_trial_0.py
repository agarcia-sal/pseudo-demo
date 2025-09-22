def main():
    # Step 1: Read input from system standard input
    input_string = read_from_standard_input()

    # Step 2: Normalize the path
    normalized_path = normalize_path(input_string)

    # Step 3: Remove leading slashes from the normalized path
    cleaned_path = remove_leading_slashes(normalized_path)

    # Step 4: Print the cleaned path
    print(cleaned_path)

def read_from_standard_input():
    return input()

def normalize_path(path):
    # Assumes that path is a string
    return normalize_posix_path(path)  # Converts the path to a standard format

def remove_leading_slashes(path):
    # Assumes that path is a string
    import re
    return re.sub(r'^/+', '/', path)  # Replaces one or more leading slashes with a single slash

def normalize_posix_path(path):
    # Placeholder function for normalizing POSIX paths.
    # The actual implementation should ensure the path conforms to POSIX standards.
    return path.strip()  # Example implementation

# The entry point for the program
if __name__ == "__main__":
    main()
