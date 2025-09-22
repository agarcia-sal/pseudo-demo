import posixpath  # Import the posixpath library for path operations
import sys        # Import the sys library for reading from system input
import re         # Import the re library for regular expression operations

# Read input path from the user, stripping any surrounding whitespace
input_path = input().strip()

# Normalize the path using posixpath
normalized_path = posixpath.normpath(input_path)

# Ensure leading forward slash - replace any leading slashes with a single '/'
final_path = re.sub(r'^[/]+', '/', normalized_path)

# Output the final normalized path
print(final_path)
