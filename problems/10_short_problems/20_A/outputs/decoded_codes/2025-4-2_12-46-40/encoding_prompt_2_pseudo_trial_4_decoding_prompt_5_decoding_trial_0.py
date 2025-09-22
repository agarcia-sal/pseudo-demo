import os
import re

# Read input from standard input and clean the whitespace
input_path = input().strip()

# Normalize the path using os.path.normpath for proper format
normalized_path = os.path.normpath(input_path)

# Remove leading slashes by replacing occurrences of one or more slashes at the start with a single slash
normalized_path = re.sub(r'^/+', '/', normalized_path)

# Output the modified path
print(normalized_path)
