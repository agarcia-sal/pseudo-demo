# Start Program

# Step 1: Read a sequence of characters from standard input
file_path = input()

# Step 2: Remove any leading or trailing spaces from the input
file_path = file_path.strip()

# Step 3: Normalize the file path to eliminate redundant slashes
# Replacing multiple consecutive slashes with a single slash
import re
normalized_path = re.sub(r'/+', '/', file_path)

# Step 4: If normalized path begins with one or more slashes,
# replace those leading slashes with a single slash
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')

# Step 5: Display the modified file path
print(normalized_path)

# End Program
