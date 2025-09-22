# Begin Program

# Read Input: Accept a line of input from the user and remove any leading or trailing spaces.
input_string = input().strip()

# Initialize Variables:
index = 0  # To keep track of our current position in input_string
output_string = ""  # To build the resulting output

# Process Input:
while index < len(input_string):
    if input_string[index] == '.':
        # If the character at the current position is a period
        output_string += '0'  # Append '0' to output_string
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # If the next character is also a period
        output_string += '1'  # Append '1' to output_string
        index += 2  # Skip both characters
    else:
        # If the next character is not a period
        output_string += '2'  # Append '2' to output_string
        index += 2  # Skip both characters

# Output Result:
print(output_string)

# End Program
