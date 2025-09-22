# Step 1: Receive User Input
file_path = input()

# Step 2: Normalize the Path
normalized_path = file_path.strip()  # Remove leading and trailing whitespace
normalized_path = normalized_path.replace("\\", "/")  # Replace backslashes with forward slashes

# Step 3: Remove Leading Slashes
while normalized_path.startswith('/'):
    normalized_path = normalized_path[1:]  # Remove leading slashes

if len(normalized_path) > 0:
    normalized_path = '/' + normalized_path  # Add a single leading slash if the path is not empty

# Step 4: Display the Final Path
print(normalized_path)
