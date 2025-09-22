import os
import sys
import re

# Read input
input_string = input().strip()

# Normalize path
normalized_path = os.path.normpath(input_string)

# Adjust leading slashes
adjusted_path = re.sub(r'^/+', '/', normalized_path)

# Output result
print(adjusted_path)
