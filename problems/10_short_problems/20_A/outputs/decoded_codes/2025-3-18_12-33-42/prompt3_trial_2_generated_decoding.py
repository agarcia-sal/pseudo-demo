import os

def main():
    # Step 1: Read input from standard input, ensuring there are no leading or trailing spaces
    input_string = input().strip()

    # Step 2: Normalize the path to ensure it uses the correct format for POSIX file paths
    normalized_path = os.path.normpath(input_string)

    # Step 3: Remove any leading slashes and ensure there's only one leading slash if needed
    cleaned_path = '/' + normalized_path.lstrip('/')

    # Step 4: Output the cleaned path
    print(cleaned_path)

if __name__ == "__main__":
    main()
