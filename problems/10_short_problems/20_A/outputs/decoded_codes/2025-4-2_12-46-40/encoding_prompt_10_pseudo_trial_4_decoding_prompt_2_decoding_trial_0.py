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
    return input()  # Assuming input() captures the string as required

def normalize_path(path):
    return normalize_posix_path(path)  # Converts the path to a standard format

def remove_leading_slashes(path):
    import re
    return re.sub(r'^/+', '/', path)  # Replaces one or more leading slashes with a single slash

def normalize_posix_path(path):
    # Implementation of normalization logic
    # For demonstration, we are just returning the path back.
    # In a real scenario, you would implement the actual normalization logic here.
    return path

# Execute the main function
if __name__ == "__main__":
    main()
