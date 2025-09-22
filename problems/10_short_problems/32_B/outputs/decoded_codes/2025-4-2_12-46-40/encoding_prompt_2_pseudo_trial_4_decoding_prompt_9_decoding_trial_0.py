# Read a single line of input and trim any leading or trailing white space
input_string = input().strip()

# Initialize current index and output string
current_index = 0
output_string = ""

# Process the input string
while current_index < len(input_string):
    # Check if the current character is a dot
    if input_string[current_index] == '.':
        output_string += '0'  # Append '0' to the output string
        current_index += 1  # Move to the next character
    else:
        # Check if the next character exists and if it is a dot
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            output_string += '1'  # Append '1' for a dot found after the current character
            current_index += 2  # Move past both characters
        else:
            output_string += '2'  # Append '2' if the next character is not a dot
            current_index += 2  # Move past both characters

# Print the result
print(output_string)
