import re

def NormalizeFilePath():
    # Step 1.1: Read the input file path from standard input
    # Using sys.stdin to allow the user to input a path
    file_path = input().strip()

    # Step 1.2: Normalize the path to eliminate redundant parts
    # Use regex to reduce multiple slashes to a single slash
    normalized_path = re.sub(r'/+', '/', file_path)

    # Step 1.3: Ensure the output starts with exactly one forward slash
    # Remove leading slashes and replace with exactly one
    if normalized_path.startswith('/'):
        normalized_path = '/' + normalized_path.lstrip('/')
    else:
        normalized_path = '/' + normalized_path

    # Step 1.4: Output the modified path
    print(normalized_path)

# Call the NormalizeFilePath function to execute the normalization process
NormalizeFilePath()
