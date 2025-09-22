import os
import re

def main():
    # Step 1: Read input from user
    user_input = input().strip()  # Trim whitespace from input string

    # Step 2: Normalize the path
    normalized_path = os.path.normpath(user_input)

    # Step 3: Adjust leading slashes
    adjusted_path = re.sub(r'^/+','/', normalized_path)

    # Step 4: Output the final adjusted path
    print(adjusted_path)

if __name__ == "__main__":
    main()
