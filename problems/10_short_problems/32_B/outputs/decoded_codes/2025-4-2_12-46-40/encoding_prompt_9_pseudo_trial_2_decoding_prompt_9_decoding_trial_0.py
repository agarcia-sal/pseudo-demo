# Start Program

# Receive Input
input_string = input().strip()  # Read the input string and remove unnecessary whitespace

# Initialize Variables
current_index = 0  # Track the position within the input string
output_string = ""  # Store the resulting numerical representation

# Process Input String
while current_index < len(input_string):
    # Check if the current character is a dot (.)
    if input_string[current_index] == '.':
        output_string += '0'  # Append '0' for a single dot
        current_index += 1  # Move to the next character
    # Check if there is a dot next to the current character
    elif (current_index + 1 < len(input_string)) and (input_string[current_index + 1] == '.'):
        output_string += '1'  # Append '1' for a sequence of two dots
        current_index += 2  # Move past the two dots
    else:
        output_string += '2'  # Append '2' for any other character
        current_index += 2  # Move past the current character and the next one if any

# Output Result
print(output_string)  # Print the final numerical representation

# End Program
