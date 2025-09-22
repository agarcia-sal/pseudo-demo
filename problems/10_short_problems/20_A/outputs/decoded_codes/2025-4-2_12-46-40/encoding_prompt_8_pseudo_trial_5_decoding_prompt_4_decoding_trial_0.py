import os

def main():
    # Step 1: Read the input from the user
    input_path = input().strip()  # Read and strip any extra spaces around input

    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(input_path)  # Normalize path using standard libraries

    # Step 3: Adjust the path
    if normalized_path.startswith('/'):
        output_path = '/' + normalized_path.lstrip('/')  # Use lstrip() to remove extra leading slashes
    else:
        output_path = normalized_path.lstrip('/')  # Just remove leading slashes if there's no leading slash

    # Step 4: Print the result
    print(output_path)

if __name__ == "__main__":
    main()
