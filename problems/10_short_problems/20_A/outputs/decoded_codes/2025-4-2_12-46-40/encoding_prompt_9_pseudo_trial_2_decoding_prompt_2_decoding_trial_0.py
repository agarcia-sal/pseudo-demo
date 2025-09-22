import os
import re

def main():
    # Step 1: Get Input
    file_path = input().strip()

    # Step 2: Normalize the Path
    normalized_path = os.path.normpath(file_path)

    # Step 3: Ensure Proper Format
    if normalized_path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        normalized_path = re.sub(r'^/+','/', normalized_path)
    else:
        # If it doesn't start with a slash, add one
        normalized_path = '/' + normalized_path

    # Step 4: Display Result
    print(normalized_path)

# Execute the main function
if __name__ == "__main__":
    main()
