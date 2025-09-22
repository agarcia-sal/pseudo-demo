# Start of the code

# Read the input from the standard input and remove any leading or trailing spaces
string = input().strip()

# Replace occurrences of the word 'dot' with the symbol '.'
string = string.replace('dot', '.')

# Replace occurrences of the word 'at' with the symbol '@'
string = string.replace('at', '@')

# If the first character is '.', prepend 'dot' to the string
if string and string[0] == '.':
    string = 'dot' + string[1:]

# Initialize a counter for '@' occurrences and an empty list for characters
counter = 0
output_characters = []
length = 0

# If the first character is '@', prepend 'at' to the string
if string and string[0] == '@':
    string = 'at' + string[1:]

# For each character in the modified string
for character in string:
    if character == '@':
        # If there was a previous occurrence of '@', append 'at'; reset counter
        if counter > 0:
            output_characters.append('at')
            counter = 1
        else:
            # Otherwise, append '@' to output_characters; set counter to 1
            output_characters.append('@')
            counter = 1
    else:
        # Append the current character to the output list
        output_characters.append(character)

# Join the characters in output_characters into a single string
output_string = ''.join(output_characters)

# If the last character of the output_string is '.', replace it with 'dot'
if output_string and output_string[-1] == '.':
    output_string = output_string[:-1] + 'dot'

# Print the final transformed string
print(output_string)

# End of the code
