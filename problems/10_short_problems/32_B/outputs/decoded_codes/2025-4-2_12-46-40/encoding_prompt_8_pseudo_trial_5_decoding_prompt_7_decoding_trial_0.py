# Import necessary libraries for input
import sys

# Read input from standard input and strip any extra spaces
input_string = input().strip()

# Initialize variable to keep track of the current index in the input string
index = 0
# Initialize result as an empty string to accumulate the translated output
result = ""

# Process the input string based on defined rules
while index < len(input_string):
    # Check if the current character is a dot ('.')
    if input_string[index] == '.':
        result += '0'  # Translate single dot to '0'
        index += 1  # Move to the next character
    # Check if the next character is also a dot (if the index allows for it)
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Translate two dots together to '1'
        index += 2  # Move forward by two characters
    else:
        result += '2'  # Any other character translates to '2'
        index += 2  # Move forward by two characters

# Output the result containing the numeric representation
print(result)
