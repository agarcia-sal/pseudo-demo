# Step 1: Import libraries for path manipulation and regex processing
import posixpath
import re

# Step 2: Read input path
input_path = input()  # Read input from user
stripped_path = input_path.strip()  # Remove leading and trailing whitespace from input_path

# Step 3: Normalize the path
normalized_path = posixpath.normpath(stripped_path)  # Normalize the path

# Step 4: Adjust leading slashes
cleaned_path = re.sub(r'^(/{2,})', '/', normalized_path)  # Replace multiple leading slashes with a single slash

# Step 5: Output the cleaned-up path
print(cleaned_path)  # Print the cleaned path
