# Begin the program

# Read the input string from the user
input_string = input()

# Initialize variables
index = 0
output_string = ""

# Loop through the input string until we reach the end
while index < len(input_string):
    # Check if the current character is '.'
    if input_string[index] == '.':
        # If current character is a '.', append '0' to output_string
        output_string += '0'
        index += 1  # Increase index by 1
    # Check if the next character is also '.'
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # If next character is also '.', append '1' to output_string
        output_string += '1'
        index += 2  # Increase index by 2
    else:
        # Otherwise, append '2' to output_string
        output_string += '2'
        index += 2  # Increase index by 2

# Output the result
print(output_string)

# End the program
