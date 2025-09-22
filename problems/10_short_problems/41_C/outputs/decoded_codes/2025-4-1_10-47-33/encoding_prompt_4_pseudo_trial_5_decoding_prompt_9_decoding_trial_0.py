def replace_all(string, old, new):
    # Replace all occurrences of 'old' with 'new' in 'string'
    return string.replace(old, new)

# Read a line of input and remove leading and trailing spaces
input_string = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
transformed_string = replace_all(input_string, 'dot', '.')
transformed_string = replace_all(transformed_string, 'at', '@')

# If the first character is '.', prepend 'dot'
if transformed_string.startswith('.'):
    transformed_string = 'dot' + transformed_string[1:]

# Initialize a counter and a list to hold characters
counter = 0
character_list = []

# If the string starts with '@', prepend 'at'
if transformed_string.startswith('@'):
    transformed_string = 'at' + transformed_string[1:]

# Iterate through each character in the transformed string
for character in transformed_string:
    if character == '@':
        # If we have already processed an '@', replace it with 'at'
        if counter > 0:
            character_list.append('at')
            counter = 1
        else:
            character_list.append('@')
            counter = 1
    else:
        # Add non-special characters to the list
        character_list.append(character)

# Join the characters in the list to form the final string
final_string = ''.join(character_list)

# If the last character is '.', replace it with 'dot'
if final_string.endswith('.'):
    final_string = final_string[:-1] + 'dot'

# Print the final transformed string
print(final_string)
