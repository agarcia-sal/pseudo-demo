# Import required libraries
import sys

# Read input and remove extra spaces
input_string = input().strip()

# Initialize variables
index = 0
result = ""

# Process the input string
while index < len(input_string):
    # If the current character is a dot
    if input_string[index] == '.':
        result += '0'  # Append '0' to result
        index += 1     # Move to next character
    # If the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to result
        index += 2     # Skip next character
    else:
        result += '2'  # Append '2' to result
        index += 2     # Skip next character

# Output the result
print(result)
