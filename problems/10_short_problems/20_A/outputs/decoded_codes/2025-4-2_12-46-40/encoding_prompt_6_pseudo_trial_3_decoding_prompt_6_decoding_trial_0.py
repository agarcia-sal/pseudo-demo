# Start of the code

# Step 1: Read input from standard input (user input)
input_string = input()

# Step 2: Remove leading and trailing whitespace from input_string
trimmed_input_string = input_string.strip()

# Step 3: Normalize the path to a standard format
# In Python, we can use os.path.normpath for normalization
import os
normalized_path = os.path.normpath(trimmed_input_string)

# Step 4: Replace sequences of leading slashes with a single slash
# We can use a regular expression to achieve this
import re
updated_path = re.sub(r'^/+', '/', normalized_path)

# Step 5: Output the final transformed path
print(updated_path)

# End of the code
