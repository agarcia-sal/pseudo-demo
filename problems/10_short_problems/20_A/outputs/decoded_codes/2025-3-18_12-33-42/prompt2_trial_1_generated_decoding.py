import re

# Step 1: Read input and normalize the file path
rawFilePath = input().strip()  # Read input and remove leading/trailing whitespace

# Normalize the file path (for example, replace backslashes with forward slashes)
# Since 'os.path.normpath' can be used to normalize path formats, we leverage it here.
normalizedFilePath = rawFilePath.replace("\\", "/")  # example normalization

# Step 2: Remove leading slashes using regular expressions
# The pattern removes multiple leading slashes and replaces them with a single slash
finalFilePath = re.sub(r'^/+', '/', normalizedFilePath)

# Step 3: Output the result
print(finalFilePath)
