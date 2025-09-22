import os

def main():
    # Step 1: Read the input from the user
    input_path = input().strip()  # Read the entire input and remove extra spaces

    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(input_path)  # Normalize the input path using os.path.normpath

    # Step 3: Adjust the path
    if normalized_path.startswith('/'):
        # Replace multiple leading slashes with a single leading slash
        output_path = '/' + normalized_path.lstrip('/')
    else:
        output_path = normalized_path.lstrip('/')  # No leading slash if it doesn't start with one

    # Step 4: Print the result
    print(output_path)

# The main function will be executed when the script runs
if __name__ == "__main__":
    main()
