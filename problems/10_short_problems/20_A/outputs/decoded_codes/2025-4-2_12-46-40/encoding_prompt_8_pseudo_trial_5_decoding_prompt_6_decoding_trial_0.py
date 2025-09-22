import os

# Step 1: Read the input from the user
# This input represents a file path
input_path = input().strip()  # Remove any extra spaces around the input

# Step 2: Normalize the file path using os.path.normpath
normalized_path = os.path.normpath(input_path)  # Normalize the path according to POSIX standards

# Step 3: Adjust the path
# Replace all sequences of leading slashes with a single leading slash
if normalized_path.startswith('/'):
    output_path = '/' + normalized_path.lstrip('/')  # Keep one leading slash
else:
    output_path = normalized_path.lstrip('/')  # No leading slashes

# Step 4: Print the result
print(output_path)  # Display the final adjusted path to the user
