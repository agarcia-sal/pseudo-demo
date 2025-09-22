# Read a line of input and remove extra spaces
input_string = input().strip()

# Initialize index to track position in the input string
index = 0

# Initialize output string to store the result
output_string = ""

# Process each character in the input string
while index < len(input_string):
    # Check if the current character is '.'
    if input_string[index] == '.':
        output_string += '0'  # Add '0' for single dot
        index += 1  # Move to next character
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        output_string += '1'  # Add '1' for 'dot dot'
        index += 2  # Move past this pair of characters
    else:
        output_string += '2'  # Add '2' for any other character
        index += 2  # Move past this pair of characters

# Print the final output string
print(output_string)
