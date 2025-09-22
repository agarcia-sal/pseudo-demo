import os  # Import the module for path handling
import re  # Import the module for regular expressions

def main():
    # Step 2: Read input from the user and trim whitespace
    input_path = input().strip()

    # Step 3: Normalize the path to ensure it uses the correct format
    normalized_path = os.path.normpath(input_path)

    # Step 4: Adjust leading slashes using regular expressions
    adjusted_path = re.sub(r'^/+','/', normalized_path)

    # Step 5: Output the final adjusted path
    print(adjusted_path)

if __name__ == "__main__":
    main()
