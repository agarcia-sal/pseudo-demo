# Importing necessary libraries
import sys

# Reading input from standard input and cleaning extra spaces
input_string = input().strip()

# Initializing variables
index = 0
result = ""

# Processing the input string
while index < len(input_string):
    # If the current character is a dot
    if input_string[index] == '.':
        result += '0'  # Append '0' to result
        index += 1  # Move to the next character
    # If the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to result
        index += 2  # Skip both characters
    else:
        result += '2'  # For any other character, append '2'
        index += 2  # Skip both characters

# Output the result
print(result)
