# Read input from the user and strip any surrounding whitespace
user_input = input().strip()

# Replace 'dot' with '.' in the input
user_input = user_input.replace('dot', '.')

# Replace 'at' with '@' in the input
user_input = user_input.replace('at', '@')

# If the first character is '.', add 'dot' at the beginning
if user_input.startswith('.'):
    user_input = 'dot' + user_input[1:]

# Initialize a variable to count occurrences of '@'
occurrence_count = 0

# Initialize a list to store processed characters
processed_characters = []

# Process the input string character by character
for current_char in user_input:
    if current_char == '@':
        if occurrence_count > 0:
            processed_characters.append('at')
            occurrence_count = 1
        else:
            processed_characters.append('@')
            occurrence_count = 1
    else:  # For characters other than '@'
        processed_characters.append(current_char)

# Join the list of processed characters into a string
final_output = ''.join(processed_characters)

# If the last character is '.', replace it with 'dot'
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'

# Print the final transformed output
print(final_output)
