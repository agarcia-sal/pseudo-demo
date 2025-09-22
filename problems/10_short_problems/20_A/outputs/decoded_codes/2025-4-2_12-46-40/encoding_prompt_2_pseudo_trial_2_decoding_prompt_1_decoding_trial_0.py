# Step 1: Start (not explicit in Python, but we begin the script)

# Step 2: Define Input
input_path = input()  # Read a line of input from the user

# Step 3: Process Input
normalized_path = input_path.strip()  # Remove leading or trailing whitespace

# Normalize the path (this can be done using os.path.normpath in practical applications)
import os
normalized_path = os.path.normpath(normalized_path) 

# Step 4: Adjust Path Format
if normalized_path.startswith('/'):
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace multiple forward slashes with a single one

# Step 5: Output Result
print(normalized_path)  # Display the modified file path to the user

# Step 6: End (not explicit in Python, but the script ends here)
