# BEGIN

# Read input from standard input (user or file) and remove any leading/trailing whitespace
inputString = input()  # Read input
trimmedInputString = inputString.strip()  # Remove leading and trailing whitespace

# Normalize the path, converting it to a standard format
normalizedPath = normalized_path(trimmedInputString)  # Assuming a function for normalization

# Replace any sequence of leading slashes with a single slash
updatedPath = updated_leading_slashes(normalizedPath)  # Assuming a function for replacing slashes

# Output the final transformed path
print(updatedPath)

# END


import os

def normalized_path(path):
    # Normalize the path (using os.path.normpath or similar logic)
    return os.path.normpath(path)

def updated_leading_slashes(path):
    # Replace sequences of leading slashes with a single slash
    while path.startswith('//'):  # Continue until it's not starting with two or more slashes
        path = path.lstrip('/')  # Remove leading slashes
    return '/' + path if path else path  # Ensure at least one leading slash

# Main execution
inputString = input()  # Read input
trimmedInputString = inputString.strip()  # Remove leading and trailing whitespace

normalizedPath = normalized_path(trimmedInputString)  # Normalize the path
updatedPath = updated_leading_slashes(normalizedPath)  # Replace leading slashes

print(updatedPath)  # Output the final transformed path
