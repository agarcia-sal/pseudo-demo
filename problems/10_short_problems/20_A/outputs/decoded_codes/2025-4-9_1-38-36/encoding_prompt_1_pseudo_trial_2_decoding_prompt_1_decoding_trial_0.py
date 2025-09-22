# Begin Program

# Step 1: Read the input from the user
rawFilePath = input()

# Step 2: Remove unnecessary slashes from the input
normalizedPath = rawFilePath.strip('/')  # Remove leading and trailing slashes
normalizedPath = '/'.join(filter(None, normalizedPath.split('/')))  # Normalize internal slashes

# Step 3: Output the cleaned-up file path
print(normalizedPath)

# End Program
