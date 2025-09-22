import os
import re

def main():
    # Step 1: Read Input
    input_path = input().strip()  # Get input and remove leading/trailing whitespace

    # Step 2: Normalize Path
    normalized_path = os.path.normpath(input_path)  # Normalize path format

    # Step 3: Remove Leading Slashes
    # Replace leading slashes with a single slash
    normalized_path = re.sub(r'^/+','/', normalized_path)

    # Step 4: Output Result
    print(normalized_path)  # Display modified path

if __name__ == "__main__":
    main()
