# Read input from standard input
input_string = input().strip()  # Remove leading and trailing whitespace

# Replace occurrences of specific words with symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# If the first character is '.', prepend 'dot' to the string
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize a counter and an empty list to hold characters
counter = 0
character_list = []
length = 0

# If the first character is '@', prepend 'at' to the string
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Process each character in input_string
for character in input_string:
    if character == '@':
        if counter > 0:
            character_list.append('at')  # Append 'at' if counter is greater than 0
            counter = 1
        else:
            character_list.append('@')  # Append '@' and set counter
            counter = 1
    else:
        character_list.append(character)  # Append the character to the list

# Join the list of characters into a single string
processed_string = ''.join(character_list)

# If the last character is '.', replace it with 'dot'
if processed_string.endswith('.'):
    processed_string = processed_string[:-1] + 'dot'  # Replace last '.' with 'dot'

# Output the final processed string
print(processed_string)
