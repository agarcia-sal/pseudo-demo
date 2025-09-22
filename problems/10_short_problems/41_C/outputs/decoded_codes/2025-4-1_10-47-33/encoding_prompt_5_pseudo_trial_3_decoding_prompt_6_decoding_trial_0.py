# Start of the program

# Read input from the user
input_string = input()

# Remove unnecessary spaces from the beginning and end of the string
input_string = input_string.strip()

# Replace occurrences of 'dot' with '.' (representing a period)
input_string = input_string.replace('dot', '.')

# Replace occurrences of 'at' with '@' (representing an at sign)
input_string = input_string.replace('at', '@')

# If the first character is a period, prefix the string with 'dot'
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize a counter and an empty list to hold processed characters
counter = 0
processed_list = []

# If the first character is '@', prefix the string with 'at'
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Iterate through each character in the modified input string
for character in input_string:
    # Check if the character is '@'
    if character == '@':
        # If '@' has been encountered before, append 'at' to the list
        if counter > 0:
            processed_list.append('at')
            counter = 1
        else:
            # Otherwise, append '@' to the list
            processed_list.append('@')
            counter = 1
    else:
        # For any other character, simply append it to the list
        processed_list.append(character)

# Join the processed characters back into a single string
final_string = ''.join(processed_list)

# If the last character is a period, replace it with 'dot'
if final_string.endswith('.'):
    final_string = final_string[:-1] + 'dot'

# Output the final string
print(final_string)

# End of the program
