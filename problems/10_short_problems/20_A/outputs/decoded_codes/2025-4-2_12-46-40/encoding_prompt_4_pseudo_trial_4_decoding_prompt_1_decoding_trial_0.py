# Read a file path input from standard input
INPUT_PATH = input()

# Normalize the file path by removing redundant separators
import os
NORMALIZED_PATH = os.path.normpath(INPUT_PATH)

# Replace any leading slashes with a single leading slash
CLEANED_PATH = NORMALIZED_PATH.lstrip('/').rstrip('/')  # Removing leading slashes
CLEANED_PATH = '/' + CLEANED_PATH if CLEANED_PATH else '/'  # Ensure there's at least one leading slash

# Output the cleaned path
print(CLEANED_PATH)
