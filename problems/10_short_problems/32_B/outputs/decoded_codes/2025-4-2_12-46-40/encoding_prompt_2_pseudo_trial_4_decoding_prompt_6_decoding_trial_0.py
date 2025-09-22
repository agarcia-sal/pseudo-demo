# Read a single line of input, trimming any leading or trailing whitespace
input_string = input().strip()

# Initialize an index variable and an empty output string
current_index = 0
output_string = ""

# Process the input string based on given rules
while current_index < len(input_string):
    if input_string[current_index] == '.':
        # If the current character is a dot, append '0' to output_string
        output_string += '0'
        # Move to the next character
        current_index += 1
    else:
        # Check the next character
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # If the next character is a dot, append '1' to output_string
            output_string += '1'
            # Move to the next two characters
            current_index += 2
        else:
            # Otherwise, append '2' to output_string
            output_string += '2'
            # Move to the next two characters
            current_index += 2

# Output the resulting transformation of the input string
print(output_string)
