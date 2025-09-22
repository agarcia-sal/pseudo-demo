# Read a line of input that contains a string of characters
input_string = input()  
# Initialize the current index to 0 and an empty output string
current_index = 0
output_string = ""

# Processing loop until the current index reaches the end of the input string
while current_index < len(input_string):
    # Check the character at the current index
    if input_string[current_index] == ".":
        # If it is a dot, append '0' to the output string
        output_string += '0'
        # Move to the next character
        current_index += 1
    # Check if there is a next character and if it is also a dot
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == ".":
        # If the next character is a dot, append '1' to the output string
        output_string += '1'
        # Skip the next character
        current_index += 2
    else:
        # Otherwise, append '2' for any non-dot character and skip the next character
        output_string += '2'
        current_index += 2  # Always skip the next character

# Output the resulting output string
print(output_string)
