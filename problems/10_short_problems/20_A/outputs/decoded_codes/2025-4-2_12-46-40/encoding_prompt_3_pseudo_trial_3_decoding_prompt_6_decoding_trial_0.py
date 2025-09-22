import os
import re

# Read input from the user
user_input = input()  # Getting user input

# Remove leading and trailing whitespace from the input
trimmed_input = user_input.strip()  # Trimming whitespace

# Normalize the path by eliminating redundant separators and up-level references
normalized_path = os.path.normpath(trimmed_input)  # Normalizing the file path

# Replace multiple leading slashes with a single leading slash
final_path = re.sub(r'//+', '/', normalized_path)  # Replacing multiple leading slashes

# Output the final normalized path
print(final_path)  # Printing the final normalized path
