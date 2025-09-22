import os

def main():
    # Step 1: Read the input from the user
    input_path = input().strip()  # Read input and remove extra spaces

    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(input_path)  # Normalize the path

    # Step 3: Adjust the path
    # Replace multiple leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        output_path = '/' + normalized_path.lstrip('/')
    else:
        output_path = normalized_path.lstrip('/')

    # Step 4: Print the result
    print(output_path)

# Entry point of the program
if __name__ == "__main__":
    main()
