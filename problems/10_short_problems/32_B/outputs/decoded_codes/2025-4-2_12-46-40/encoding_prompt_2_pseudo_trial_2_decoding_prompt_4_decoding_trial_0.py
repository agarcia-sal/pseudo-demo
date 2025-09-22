# Read a line of input containing encoded information
input_string = input()

# Initialize variables
current_index = 0
output_string = ""

# Processing loop
while current_index < len(input_string):
    # Check the character at the current index
    current_char = input_string[current_index]
    
    if current_char == '.':
        output_string += '0'  # Append '0' for a single dot
        current_index += 1     # Move to the next character
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
        output_string += '1'  # Append '1' for two consecutive dots
        current_index += 2     # Skip the next character
    else:
        output_string += '2'  # Append '2' for a non-dot character
        current_index += 2     # Skip the next character

# Output the resulting output string
print(output_string)
