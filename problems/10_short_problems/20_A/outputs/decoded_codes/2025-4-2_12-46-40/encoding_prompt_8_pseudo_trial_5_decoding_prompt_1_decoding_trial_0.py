import os

# Step 1: Read the input from the user
input_path = input().strip()  # This reads the entire input and removes any extra spaces

# Step 2: Normalize the file path
normalized_path = os.path.normpath(input_path)  # Normalize using standard path normalization rules

# Step 3: Adjust the path
output_path = '/' + normalized_path.lstrip('/')  # Replace all sequences of leading slashes with a single slash

# Step 4: Print the result
print(output_path)
