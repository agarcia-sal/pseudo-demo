import os

def main():
    # Step 2: Define Input
    user_input = input()

    # Step 3: Process Input
    normalized_path = os.path.normpath(user_input.strip())

    # Step 4: Adjust Path Format
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 5: Output Result
    print(normalized_path)

# Entry point to run the program
if __name__ == "__main__":
    main()
