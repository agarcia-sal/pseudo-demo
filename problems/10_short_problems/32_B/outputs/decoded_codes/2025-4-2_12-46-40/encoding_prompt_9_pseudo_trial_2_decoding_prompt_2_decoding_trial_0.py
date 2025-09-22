# Start Program

# Receive Input
input_string = input().strip()

# Initialize Variables
current_index = 0
output_string = ""

# Process Input String
while current_index < len(input_string):
    if input_string[current_index] == '.':
        output_string += '0'
        current_index += 1
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
        output_string += '1'
        current_index += 2
    else:
        output_string += '2'
        current_index += 2

# Output Result
print(output_string)

# End Program
