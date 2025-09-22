# Read a single line of input and trim whitespace
input_string = input().strip()

# Initialize the index and output string
current_index = 0
output_string = ""

# Process the input string according to the given rules
while current_index < len(input_string):
    # Check if the current character is a dot
    if input_string[current_index] == '.':
        # Append '0' to the output string for a dot
        output_string += '0'
        # Move to the next character
        current_index += 1
    else:
        # Check the next character
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            # Append '1' if the next character is a dot
            output_string += '1'
            # Move to the next two characters
            current_index += 2
        else:
            # Append '2' if the next character is not a dot
            output_string += '2'
            # Move to the next two characters
            current_index += 2

# Print the final output string
print(output_string)
