# Read input from the user
input_string = input()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
input_string = input_string.replace('dot', '.').replace('at', '@')

# Check if the first character is a dot
if input_string.startswith('.'):
    # Prepend 'dot' to the string
    input_string = 'dot' + input_string[1:]

# Initialize the counter for '@' occurrences
occurrence_counter = 0
# Initialize an empty list to collect characters
character_list = []

# Check if the first character is '@'
if input_string.startswith('@'):
    # Prepend 'at' to the string
    input_string = 'at' + input_string[1:]

# Loop through each character in the modified input string
for character in input_string:
    # Check if the character is '@'
    if character == '@':
        # If '@' has already occurred before
        if occurrence_counter > 0:
            # Append 'at' to the list
            character_list.append('at')
            occurrence_counter = 1  # Update counter
        else:
            # Append '@' to the list
            character_list.append('@')
            occurrence_counter = 1  # Update counter
    else:
        # Append the character to the list
        character_list.append(character)

# Join the list of characters into a single string
result_string = ''.join(character_list)

# Check if the last character is a dot
if result_string.endswith('.'):
    # Replace the last '.' with 'dot'
    result_string = result_string[:-1] + 'dot'

# Print the final modified string
print(result_string)
