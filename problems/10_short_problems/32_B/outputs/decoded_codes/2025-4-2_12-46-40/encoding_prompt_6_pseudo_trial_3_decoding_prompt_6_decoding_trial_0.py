# This program processes a string to generate a new output based on specific rules involving the character '.'

# Read input string from standard input and remove unnecessary whitespace
input_string = input().strip()

# Initialize an index to track current position in the string
current_index = 0

# Initialize an empty string to build the output
output_string = ''

# Continue processing the input string until the whole string is examined
while current_index < len(input_string):
    # Check for the current character
    if input_string[current_index] == '.':
        # If the current character is '.', add '0' to output and move to the next character
        output_string += '0'
        current_index += 1
    else:
        # Check the next character in the string
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # If next character is also '.', add '1' to output and move ahead by two characters
            output_string += '1'
            current_index += 2
        else:
            # If neither of the two characters is '.', add '2' to output and move ahead by two characters
            output_string += '2'
            current_index += 2

# Output the final constructed string
print(output_string)
