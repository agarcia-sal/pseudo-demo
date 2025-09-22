import os

def normalize_file_path():
    # Step 2: Read a line of input from the user
    file_path = input().strip()  # Remove leading or trailing whitespace

    # Step 3: Normalize the file path
    normalized_path = os.path.normpath(file_path)

    # Step 4: Adjust path format
    if normalized_path.startswith("/"):
        normalized_path = "/" + normalized_path.lstrip("/")  # Ensure it starts with a single slash

    # Step 5: Output the result
    print(normalized_path)

# Step 6: Start the program
normalize_file_path()
