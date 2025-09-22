import os

# Read a file path input from standard input
INPUT_PATH = input()

# Normalize the file path by removing redundant separators
NORMALIZED_PATH = os.path.normpath(INPUT_PATH)

# Replace any leading slashes with a single leading slash
if NORMALIZED_PATH.startswith('/'):
    # Count the number of leading slashes
    leading_slashes = len(NORMALIZED_PATH) - len(NORMALIZED_PATH.lstrip('/'))
    # If more than one leading slash, replace with a single one
    if leading_slashes > 1:
        CLEANED_PATH = '/' + NORMALIZED_PATH.lstrip('/')
    else:
        CLEANED_PATH = NORMALIZED_PATH
else:
    CLEANED_PATH = NORMALIZED_PATH

# Output the cleaned path
print(CLEANED_PATH)
