import os

def normalize_file_path():
    # Step 1: Read the file path from standard input and remove extra spaces
    file_path = input().strip()

    # Step 2: Normalize the file path using the system's path conventions
    normalized_path = os.path.normpath(file_path)

    # Step 3: Remove leading slashes by replacing with a single slash
    final_path = normalized_path.lstrip('/')

    # Ensure the final path starts with a leading slash
    final_path = '/' + final_path if final_path else final_path

    # Step 4: Output the result
    print(final_path)

# Example of how to test the function:
# The following line can be commented/uncommented for direct testing
# normalize_file_path()
