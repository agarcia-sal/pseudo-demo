# Program to process an email address format from input

# Read input from standard input and remove leading/trailing whitespace
email_input = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
email_input = email_input.replace('dot', '.')
email_input = email_input.replace('at', '@')

# If the first character is a dot, prepend 'dot'
if email_input.startswith('.'):
    email_input = 'dot' + email_input[1:]

# Initialize a counter for '@' symbols and a list for characters
at_counter = 0
char_list = []
l = 0  # Not used but initialized to match pseudocode

# If the first character is an '@', prepend 'at'
if email_input.startswith('@'):
    email_input = 'at' + email_input[1:]

# Iterate through each character in the modified email input
for character in email_input:
    if character == '@':
        # Check if there is already an '@' in the list
        if at_counter > 0:
            char_list.append('at')
            at_counter = 1
        else:
            char_list.append('@')
            at_counter = 1
    else:
        char_list.append(character)

# Convert the list of characters back to a string
formatted_email = ''.join(char_list)

# If the last character is a dot, replace it with 'dot'
if formatted_email.endswith('.'):
    formatted_email = formatted_email[:-1] + 'dot'

# Output the final result
print(formatted_email)
