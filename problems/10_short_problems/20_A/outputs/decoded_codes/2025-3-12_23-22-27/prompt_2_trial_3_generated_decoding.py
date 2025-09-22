# Start Program

# Step 1: Read a sequence of characters from standard input
file_path = input()
# Step 2: Remove any leading or trailing spaces from the input
file_path = file_path.strip()

# Step 3: Adjust the file path to eliminate redundant slashes
# Normalize the path
normalized_path = []
for part in file_path.split('/'):
    if part:  # Only add non-empty parts
        normalized_path.append(part)

# Join the normalized parts with a single slash
normalized_path = '/' + '/'.join(normalized_path)

# Step 4: Display the modified file path
print(normalized_path)

# End Program
