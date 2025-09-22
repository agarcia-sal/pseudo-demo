import os
import re

def normalize_and_clean_file_path():
    # Read input from standard input
    raw_input = input().strip()

    # Normalize the path using os.path.normpath
    normalized_path = os.path.normpath(raw_input)

    # Replace multiple leading slashes with a single leading slash
    # Using regex to substitute leading slashes
    cleaned_path = re.sub(r'^[\/]+', '/', normalized_path)

    # Print the cleaned path
    print(cleaned_path)

# Run the function
normalize_and_clean_file_path()
