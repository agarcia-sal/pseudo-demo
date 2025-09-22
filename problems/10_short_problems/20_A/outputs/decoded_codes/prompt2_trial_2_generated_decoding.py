import os

# Step 1: Start the process (implicitly starts here by defining the function)

# Step 2: Read Input
file_path = input()  # Obtain a string input from the user
file_path = file_path.strip()  # Remove leading and trailing whitespace

# Step 3: Normalize Path
normalized_path = os.path.normpath(file_path)  # Adjust the input path to normalize it

# Step 4: Modify Leading Slashes
if normalized_path.startswith('/'):  # Check if the normalized path starts with a slash
    normalized_path = '/' + normalized_path.lstrip('/')  # Replace leading slashes with a single slash

# Step 5: Output the Result
print(normalized_path)  # Display the modified file path

# End of Process (implicitly ends after printing the result)
