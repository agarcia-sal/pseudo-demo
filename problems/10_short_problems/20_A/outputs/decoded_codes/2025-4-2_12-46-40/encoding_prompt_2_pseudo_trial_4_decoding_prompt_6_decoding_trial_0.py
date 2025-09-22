import re

# Step 1: Read Input
input_path = input().strip()  # Get the entire input and remove leading/trailing whitespace

# Step 2: Normalize Path
# For the purposes of this example, we'll replace backslashes with forward slashes
normalized_path = input_path.replace('\\', '/')  # Normalize backslashes to forward slashes

# Step 3: Remove Leading Slashes
normalized_path = re.sub(r'^/+', '/', normalized_path)  # Replace leading slashes with a single slash

# Step 4: Output Result
print(normalized_path)  # Display the modified path
