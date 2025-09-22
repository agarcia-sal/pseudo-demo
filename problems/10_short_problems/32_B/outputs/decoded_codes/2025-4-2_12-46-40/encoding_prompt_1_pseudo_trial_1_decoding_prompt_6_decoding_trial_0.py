# Start the program

# Read a line of input from standard input and remove any leading or trailing whitespace
input_string = input().strip()

# Initialize an index variable to 0
current_index = 0

# Initialize an empty string variable to hold the output
result = ""

# While the current index is less than the length of input_string
while current_index < len(input_string):
    # If the character at current_index is a dot ('.')
    if input_string[current_index] == '.':
        # Append the character '0' to result
        result += '0'
        # Increment current_index by 1
        current_index += 1
    # Else If the next character at current_index + 1 is a dot ('.')
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
        # Append the character '1' to result
        result += '1'
        # Increment current_index by 2
        current_index += 2
    # Else
    else:
        # Append the character '2' to result
        result += '2'
        # Increment current_index by 2
        current_index += 2

# Output the value of result
print(result)

# End the program
