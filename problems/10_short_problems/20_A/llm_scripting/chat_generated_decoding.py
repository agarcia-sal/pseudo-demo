import sys
import posixpath
import re

# Read all input from standard input, strip leading/trailing whitespace
input_data = sys.stdin.read().strip()

# Normalize the input path using POSIX path normalization
normalized_path = posixpath.normpath(input_data)

# Replace any sequence of one or more leading slashes with a single slash
# ^/+ matches one or more slashes at the start of the string
result_path = re.sub(r'^/+', '/', normalized_path)

# Print the final processed path
print(result_path)
