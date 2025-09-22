import posixpath
import sys
import re

def process_file_path():
    # Read input from standard input and remove any leading or trailing whitespace
    input_path = sys.stdin.read().strip()

    # Normalize the file path to handle irregularities
    normalized_path = posixpath.normpath(input_path)

    # Replace multiple leading slashes with a single leading slash
    final_path = re.sub(r'^/+', '/', normalized_path)

    # Print the modified path
    print(final_path)

# Main entry point of the script
if __name__ == "__main__":
    process_file_path()
