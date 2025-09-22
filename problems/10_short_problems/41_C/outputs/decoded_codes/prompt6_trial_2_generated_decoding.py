# Begin the program

# Read the input string from the user
input_string = input()

# Replace all occurrences of 'dot' with '.' in the input string
input_string = input_string.replace('dot', '.')

# Replace all occurrences of 'at' with '@' in the input string
input_string = input_string.replace('at', '@')

# If the input string starts with '.', prepend 'dot' to it
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize a counter and an empty list to collect characters
counter = 0
character_list = []
length = 0

# If the input string starts with '@', prepend 'at' to it
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Iterate over each character in the modified input string
for character in input_string:
    if character == '@':
        # If we have found an '@' before, output 'at'
        if counter > 0:
            character_list.append('at')
            counter = 1  # Reset counter to indicate we have processed a character
        else:
            # If it's the first '@', output the character '@'
            character_list.append('@')
            counter = 1  # Set counter to indicate we've seen an '@'
    else:
        # For any other character, just add it to the list
        character_list.append(character)

# Join all elements from character_list into a single string
modified_string = ''.join(character_list)

# If the last character of the modified string is '.', replace it with 'dot'
if modified_string.endswith('.'):
    modified_string = modified_string[:-1] + 'dot'

# Output the final modified string
print(modified_string)

# End of the program
