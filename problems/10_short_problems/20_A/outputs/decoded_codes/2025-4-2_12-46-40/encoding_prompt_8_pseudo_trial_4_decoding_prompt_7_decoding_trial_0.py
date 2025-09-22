import re

def main():
    # Read the input from standard input, stripping any surrounding whitespace
    inputPath = input().strip()

    # Normalize the input path by removing unnecessary path separators
    # The regex is designed to replace multiple leading slashes with a single leading slash
    # and also collapse any internal redundant slashes
    normalizedPath = re.sub(r'(?<!^)\/+', '/', inputPath)  # Replace multiple slashes with a single slash
    normalizedPath = normalizedPath.lstrip('/')  # Remove leading slashes
    normalizedPath = '/' + normalizedPath if normalizedPath else ''  # Ensure a single leading slash if path is not empty

    # Print the normalized path to output
    print(normalizedPath)

# Start execution by calling the main function
main()
