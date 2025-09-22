# Begin the program

# Read input from standard input
user_input = input()          # Get user input
user_input = user_input.strip()  # Remove leading and trailing whitespace

# Replace words with symbols
user_input = user_input.replace('dot', '.')  # Replace 'dot' with '.'
user_input = user_input.replace('at', '@')    # Replace 'at' with '@'

# Ensure input does not start with a '.'
if user_input.startswith('.'):
    user_input = 'dot' + user_input[1:]  # Prepend 'dot' to the string

# Initialize variables
occurrence_counter = 0
modified_characters = []  # List to store modified characters

# Ensure input does not start with an '@'
if user_input.startswith('@'):
    user_input = 'at' + user_input[2:]  # Prepend 'at' to the string

# Process each character in the user_input
for character in user_input:
    if character == '@':
        if occurrence_counter > 0:
            modified_characters.append('at')  # Add 'at' to the list
            occurrence_counter = 1
        else:
            modified_characters.append('@')  # Add '@' to the list
            occurrence_counter = 1
    else:
        modified_characters.append(character)  # Add the character to the list

# Join modified characters into a single string
modified_output = ''.join(modified_characters)  # Create output string from the list

# Ensure output does not end with a '.'
if modified_output.endswith('.'):
    modified_output = modified_output[:-1] + 'dot'  # Replace the last character with 'dot'

# Print the final modified output
print(modified_output)
