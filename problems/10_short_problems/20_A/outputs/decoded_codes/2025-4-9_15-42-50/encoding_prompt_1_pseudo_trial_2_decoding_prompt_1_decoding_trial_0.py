# Step 1: Read the user input
us = input().strip()  # Reads input and trims leading/trailing whitespace

# Step 2: Normalize the path
# In Python, we can use replace to handle normalization.
nor = us.replace('\\', '/')  # Convert backslashes to slashes (normalization)

# Step 3: Remove extra leading slashes
if nor.startswith('/'):  # Check if 'nor' starts with slashes
    # Replace multiple leading slashes with a single slash
    nor = '/' + nor.lstrip('/')  # Remove leading slashes and keep one

# Step 4: Output the final result
print(nor)  # Display the final normalized path
