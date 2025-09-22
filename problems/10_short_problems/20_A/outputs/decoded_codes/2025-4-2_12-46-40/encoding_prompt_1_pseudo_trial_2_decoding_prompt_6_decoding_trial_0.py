import os

# Step 2: Get Input
input_string = input().strip()  # Read input and remove leading/trailing whitespace

# Step 3: Normalize Path
normalized_path = os.path.normpath(input_string)  # Normalize the file path

# Step 4: Clean Path
cleaned_path = '/' + normalized_path.lstrip('/').replace('//', '/')  # Clean the path

# Step 5: Output Result
print(cleaned_path)  # Print the cleaned path
