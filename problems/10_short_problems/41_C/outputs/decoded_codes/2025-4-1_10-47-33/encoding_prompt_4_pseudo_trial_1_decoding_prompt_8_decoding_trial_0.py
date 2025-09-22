# Begin
# Read input from user
input_string = input()

# Replace words with symbols
input_string = input_string.replace('dot', '.').replace('at', '@')

# Ensure the string starts with 'dot' if it begins with '.'
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]

# Initialize variables for processing
count_at_symbol = 0
processed_characters = []
length = 0

# Ensure the string starts with 'at' if it begins with '@'
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]

# Process each character in the modified string
for character in input_string:
    if character == '@':
        # Check if the character '@' appears consecutively
        if count_at_symbol > 0:
            processed_characters.append('at')
            count_at_symbol = 1
        else:
            processed_characters.append('@')
            count_at_symbol = 1
    else:
        processed_characters.append(character)

# Join processed characters into a single string
result_string = ''.join(processed_characters)

# Replace trailing '.' with 'dot'
if result_string.endswith('.'):
    result_string = result_string[:-1] + 'dot'

# Output the final processed string
print(result_string)

# End


replacements = {
    'dot': '.',
    'at': '@'
}

for old, new in replacements.items():
    input_string = input_string.replace(old, new)
