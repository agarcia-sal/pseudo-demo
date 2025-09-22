def modify_string(input_string):
    # Trim leading and trailing whitespace
    input_string = input_string.strip()

    # Replace specific substrings
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # Handle case where input string starts with '.'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables
    count_at = 0
    character_list = []

    # Handle case where input string starts with '@'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate over each character in the input string
    for character in input_string:
        if character == '@':
            if count_at > 0:
                # Add 'at' to the list if we already have an '@'
                character_list.append('at')
                count_at = 1
            else:
                # Add '@' to the list
                character_list.append('@')
                count_at = 1
        else:
            # Add the character to the list
            character_list.append(character)

    # Join character list into a string
    modified_string = ''.join(character_list)

    # Check if the last character is a '.'
    if modified_string.endswith('.'):
        modified_string = modified_string[:-1] + 'dot'

    return modified_string


# Read input from standard input
if __name__ == "__main__":
    user_input = input()
    result = modify_string(user_input)
    print(result)
