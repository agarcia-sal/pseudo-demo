# Start of the program

# Read input string from the user
string_input = input()

# Remove whitespace from the input string
string_input = string_input.strip()

# Initialize variables
current_index = 0
result_string = ""

# Process the input string
while current_index < len(string_input):
    if string_input[current_index] == '.':
        # Append '0' for a single dot
        result_string += '0'
        current_index += 1
    elif (current_index + 1 < len(string_input)) and (string_input[current_index + 1] == '.'):
        # Append '1' for two consecutive dots (dot followed by a dot)
        result_string += '1'
        current_index += 2
    else:
        # Append '2' for any other two characters (dot followed by a different character)
        result_string += '2'
        current_index += 2

# Output the result
print(result_string)

# End of the program
