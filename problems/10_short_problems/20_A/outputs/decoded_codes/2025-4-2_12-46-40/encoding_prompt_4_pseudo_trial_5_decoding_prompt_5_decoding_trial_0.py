def normalize_path(path):
    """
    Normalize the file path by replacing backslashes with forward slashes.
    """
    return path.replace('\\', '/')

def remove_leading_slashes(path):
    """
    Remove leading slashes from the file path,
    replacing multiple leading slashes with a single '/'
    """
    while path.startswith('/'):
        path = path[1:]
    return path

# Read input from standard input
input_path = input()

# Normalize the file path
normalized_path = normalize_path(input_path)

# Remove leading slashes from the normalized file path
final_path = remove_leading_slashes(normalized_path)

# Output the final modified file path
print(final_path)

# Test cases (uncomment to test)
# assert remove_leading_slashes("//home/user") == "home/user"
# assert normalize_path("C:\\folder\\file.txt") == "C:/folder/file.txt"
