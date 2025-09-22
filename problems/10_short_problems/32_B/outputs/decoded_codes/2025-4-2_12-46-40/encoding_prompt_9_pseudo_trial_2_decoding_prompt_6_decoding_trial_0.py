# Start Program

# Receive Input
input_string = input().strip()  # Read and remove any unnecessary whitespace

# Initialize Variables
current_index = 0  # Tracks the position within the input string
output_string = ""  # Stores the resulting numerical representation

# Process Input String
while current_index < len(input_string):
    if input_string[current_index] == '.':
        output_string += '0'  # Append '0' for a single dot
        current_index += 1  # Move to the next character
    elif (current_index + 1 < len(input_string)) and (input_string[current_index + 1] == '.'):
        output_string += '1'  # Append '1' for a dot followed by another dot
        current_index += 2  # Move past the next character as well
    else:
        output_string += '2'  # For any other characters, append '2'
        current_index += 2  # Move forward by two characters

# Output Result
print(output_string)  # Print the final numerical representation

# End Program
