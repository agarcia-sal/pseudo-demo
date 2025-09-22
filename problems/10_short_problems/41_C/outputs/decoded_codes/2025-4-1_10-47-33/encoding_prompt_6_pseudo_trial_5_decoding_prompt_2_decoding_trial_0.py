# Begin

# Step 1: Read a line of input and remove leading/trailing spaces
line_of_text = input().strip()

# Step 2: Replace occurrences of 'dot' with '.' and 'at' with '@'
line_of_text = line_of_text.replace('dot', '.')
line_of_text = line_of_text.replace('at', '@')

# Step 3: If the first character is a '.', prepend 'dot' to the string
if line_of_text and line_of_text[0] == '.':
    line_of_text = 'dot' + line_of_text[1:]

# Step 4: Initialize a counter and a list to hold the modified characters
character_counter = 0
modified_characters = []

# Step 5: If the first character is '@', prepend 'at' to the string
if line_of_text and line_of_text[0] == '@':
    line_of_text = 'at' + line_of_text[1:]

# Step 6: Iterate through each character in line_of_text
for character in line_of_text:
    if character == '@':
        # Check how many '@' have been processed
        if character_counter > 0:
            modified_characters.append('at')
            character_counter = 1
        else:
            modified_characters.append('@')
            character_counter = 1
    else:
        # Add the current character to the list of modified characters
        modified_characters.append(character)

# Step 7: Join all characters in modified_characters to create a string
final_output = ''.join(modified_characters)

# Step 8: If the last character is a '.', replace it with 'dot'
if final_output and final_output[-1] == '.':
    final_output = final_output[:-1] + 'dot'

# Step 9: Output the final modified string
print(final_output)

# End
