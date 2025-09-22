# Step 1: Read the user input
us = input().strip()  # Read input and trim leading/trailing whitespace

# Step 2: Normalize the path
nor = us.replace('\\', '/')  # Normalize by replacing backslashes with slashes

# Step 3: Remove extra leading slashes
if nor.startswith('/'):
    # Replace multiple leading slashes with a single slash
    nor = '/' + nor.lstrip('/')

# Step 4: Output the final result
print(nor)
