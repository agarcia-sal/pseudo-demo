# Begin the program

# Read input from the user
input_string = input()

# Replace occurrences of 'dot' with '.'
input_string = input_string.replace('dot', '.')

# Replace occurrences of 'at' with '@'
input_string = input_string.replace('at', '@')

# Check if the first character is '.', prepend 'dot' if true
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize a counter for '@' symbols and a list for building the output
at_counter = 0
output_list = []

# Check if the first character is '@', prepend 'at' if true
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Iterate through each character in the updated input_string
for character in input_string:
    
    # Check if the character is '@'
    if character == '@':
        
        # If '@' has already been added once, replace it with 'at'
        if at_counter > 0:
            output_list.append('at')   # Add 'at' to output list
            at_counter = 1              # Mark '@' has been added again
        else:
            output_list.append('@')      # Add '@' to output list
            at_counter = 1              # Mark first '@' has been added
    
    else:
        # For other characters, add them directly to the output_list
        output_list.append(character)

# Join the list of characters into a single string
final_output = ''.join(output_list)

# If the last character is '.', replace it with 'dot'
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'

# Print the final transformed output
print(final_output)

# End of the program
