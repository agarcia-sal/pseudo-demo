import os

# Read input path from standard input
input_path = input()

# Normalize the input path using POSIX standards
normalized_path = os.path.normpath(input_path)

# Remove leading slashes, ensuring at least one leading slash remains
# The lstrip('/') removes all leading slashes, we will add one back later
result_path = '/' + normalized_path.lstrip('/')

# Output the final processed path
print(result_path)
