import os
import re

# Step 1: Define a string variable to hold the user input
input_string = input().strip()  # Reading input and removing leading/trailing whitespace

# Step 2: Normalize the path
normalized_path = os.path.normpath(input_string)  # Normalizes the file path

# Step 3: Clean up leading slashes to ensure only one leading slash
cleaned_path = re.sub(r'^/{2,}', '/', normalized_path)  # Replaces multiple leading slashes with a single slash

# Step 4: Output the cleaned path
print(cleaned_path)  # Printing the final cleaned path
