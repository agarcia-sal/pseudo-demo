# Read a line of input and trim any surrounding whitespace
input_string = input().strip()

# Replace all occurrences of 'dot' with '.' and 'at' with '@'
input_string = input_string.replace('dot', '.')
input_string = input_string.replace('at', '@')

# If the first character is a '.', replace it with 'dot' + the rest of the string
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize a counter and an empty list to hold characters
at_counter = 0
character_list = []
length_of_string = 0

# If the first character is '@', replace it with 'at' + the rest of the string
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Iterate through each character in the modified input_string
for character in input_string:
    if character == '@':
        # If we've encountered '@' before, add 'at' to the list
        if at_counter > 0:
            character_list.append('at')
            at_counter = 1  # Reset counter to indicate '@' has been processed
        else:
            character_list.append('@')
            at_counter = 1  # Set counter to indicate we just processed '@'
    else:
        # If the character is not '@', add it to the list
        character_list.append(character)

# Join all characters in character_list into a single string
output_string = ''.join(character_list)

# If the last character of the output_string is '.', replace it with 'dot'
if output_string.endswith('.'):
    output_string = output_string[:-1] + 'dot'

# Print the final output_string
print(output_string)
