# Importing necessary libraries
import sys

# Read input from standard input and strip extra spaces
input_string = input().strip()

# Initialize variables
index = 0  # To track the current position in the input string
result = ""  # To store the final translated output

# Process the input string
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        result += '0'  # Translate dot to '0'
        index += 1  # Move to the next character
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Translate two dots to '1'
        index += 2  # Skip both characters
    else:
        result += '2'  # Translate anything else to '2'
        index += 2  # Skip to the next character

# Output the result
print(result)
