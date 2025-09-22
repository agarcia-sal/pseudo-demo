# Read input from standard input
input_string = input()

# Initialize index and result variable
index = 0
output = ''

# Process the input string
while index < len(input_string):  # While index is less than the length of input_string
    if input_string[index] == '.':  # Current character is '.'
        output += '0'  # Append '0' to output
        index += 1  # Increment index by 1
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check next character
        output += '1'  # Append '1' to output
        index += 2  # Increment index by 2
    else:
        output += '2'  # Append '2' to output
        index += 2  # Increment index by 2

# Display the result
print(output)
