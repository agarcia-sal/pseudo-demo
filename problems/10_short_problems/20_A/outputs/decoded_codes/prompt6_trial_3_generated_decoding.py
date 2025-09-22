import os  # For handling file paths
import re  # For using regular expressions

def main():
    # Step 1: Read input from standard input and remove extra whitespace
    file_path = input().strip()

    # Step 2: Normalize the file path
    normalized_file_path = os.path.normpath(file_path)

    # Step 3: Remove multiple leading slashes by replacing them with a single slash
    final_file_path = re.sub(r'^\/+', '/', normalized_file_path)

    # Step 4: Output the final result
    print(final_file_path)

# Run the main function
main()
