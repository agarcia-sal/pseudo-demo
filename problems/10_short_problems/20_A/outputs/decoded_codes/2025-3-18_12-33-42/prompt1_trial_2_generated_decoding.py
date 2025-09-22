# Import necessary libraries for file path manipulation and regular expression functionality
import os  # For path manipulation
import re  # For regular expressions

# Read input from the standard input
inputString = input()  # Read entire input from standard input

# Strip leading and trailing whitespace from the input
trimmedInputString = inputString.strip()  # Remove whitespace from the beginning and end

# Normalize the file path to a standard format
normalizedPath = os.path.normpath(trimmedInputString)  # Normalize the path

# Replace any occurrences of multiple leading slashes with a single leading slash
cleanedPath = re.sub(r'^/+', '/', normalizedPath)  # Replace leading slashes

# Output the final cleaned and normalized file path
print(cleanedPath)
