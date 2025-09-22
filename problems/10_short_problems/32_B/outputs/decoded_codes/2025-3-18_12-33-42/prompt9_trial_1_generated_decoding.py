# Start the Program

# Read Input
input_string = input()

# Initialize Variables
current_position = 0
result_string = ''

# Process Each Character in the String
while current_position < len(input_string):
    if input_string[current_position] == '.':
        result_string += '0'  # Append '0' for a single dot
        current_position += 1  # Move one step forward
    elif (current_position + 1 < len(input_string) and 
          input_string[current_position + 1] == '.'):
        result_string += '1'  # Append '1' for a dot followed by another dot
        current_position += 2  # Move two steps forward
    else:
        result_string += '2'  # Append '2' for any other character
        current_position += 2  # Move two steps forward

# Output the Result
print(result_string)

# End the Program
