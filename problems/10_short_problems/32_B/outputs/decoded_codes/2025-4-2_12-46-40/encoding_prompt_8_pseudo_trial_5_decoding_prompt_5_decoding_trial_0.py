# Import necessary libraries for reading input
import sys

# Read a single line of input and remove extra spaces
input_string = input().strip()

# Initialize variables
index = 0  # To track the current position in the input string
result = ""  # To store the translated numeric representation

# Process the input string
while index < len(input_string):
    # Check if the current character is a dot (.)
    if input_string[index] == '.':
        result += '0'  # Append '0' to the result
        index += 1  # Move to the next character
    
    # Check if the next character is also a dot (.)
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to the result
        index += 2  # Skip both characters
    
    # Otherwise, treat it as a single character (not a dot) 
    else:
        result += '2'  # Append '2' to the result
        index += 2  # Skip both characters

# Output the final result
print(result)
