import posixpath  # Import the posixpath library for path operations
import sys        # Import sys for reading from system input
import re         # Import re for regular expression operations

# Step 2: Read input path
inputPath = input().strip()  # Read input from system input and remove surrounding whitespace

# Step 3: Normalize the path
normalizedPath = posixpath.normpath(inputPath)  # Normalize the path using posixpath

# Step 4: Ensure leading forward slash
finalPath = re.sub(r'^[\/]+', '/', normalizedPath)  # Replace leading slashes with a single '/'

# Step 5: Output the final path
print(finalPath)  # Print the final normalized path
