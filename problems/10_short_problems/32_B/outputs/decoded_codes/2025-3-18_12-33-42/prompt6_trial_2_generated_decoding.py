# Start Program

# Read a line of input and remove any leading or trailing spaces
input_string = input().strip()  # Read input and remove whitespace

# Initialize a variable index to 0
index = 0

# Initialize an empty string to store the output
output_string = ''

# While index is less than the length of input_string
while index < len(input_string):
    # If the character at the current index is a dot ('.'):
    if input_string[index] == '.':
        output_string += '0'  # Append '0' to output_string
        index += 1  # Increment index by 1
    # Else if the next character (at index + 1) is a dot ('.'):
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        output_string += '1'  # Append '1' to output_string
        index += 2  # Increment index by 2
    # Else:
    else:
        output_string += '2'  # Append '2' to output_string
        index += 2  # Increment index by 2

# Print the output_string
print(output_string)

# End Program
