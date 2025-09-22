import os

def main():
    # Step 1: Read the input from the user
    input_path = input().strip()

    # Step 2: Normalize the file path
    normalized_path = os.path.normpath(input_path)

    # Step 3: Adjust the path
    if normalized_path.startswith('/'):
        output_path = '/' + normalized_path.lstrip('/')
    else:
        output_path = normalized_path.lstrip('/')

    # Step 4: Print the result
    print(output_path)

if __name__ == "__main__":
    main()
