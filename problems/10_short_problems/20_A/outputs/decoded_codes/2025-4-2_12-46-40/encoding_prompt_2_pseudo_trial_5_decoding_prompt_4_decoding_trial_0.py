import os

def normalize_path():
    # Step 1: Read Input
    user_input = input().strip()  # Accept input as a string and remove leading/trailing whitespace

    # Step 2: Normalize Path
    normalized_path = os.path.normpath(user_input)  # Use os.path.normpath() to normalize the file path

    # Step 3: Modify Leading Slashes
    if normalized_path.startswith('/'):  # Check for leading slashes
        # Replace multiple leading slashes with a single '/'
        normalized_path = '/' + normalized_path.lstrip('/')

    # Step 4: Output Result
    print(normalized_path)  # Display the modified path

# Example to run the function
normalize_path()
