def format_string():
    # Read input string from standard input and remove surrounding whitespace
    original_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    original_string = original_string.replace('dot', '.').replace('at', '@')

    # If the string starts with a '.', prefix it with 'dot'
    if original_string.startswith('.'):
        original_string = 'dot' + original_string[1:]

    counter = 0
    modified_characters = []

    # If the string starts with '@', prefix it with 'at'
    if original_string.startswith('@'):
        original_string = 'at' + original_string[1:]

    # Loop through each character in the modified string
    for character in original_string:
        # Check if the current character is '@'
        if character == '@':
            # If it's not the first '@' encountered
            if counter > 0:
                modified_characters.append('at')
                counter += 1
            else:
                modified_characters.append('@')
                counter += 1
        else:
            modified_characters.append(character)

    # Join all characters in modified_characters into a final string
    final_string = ''.join(modified_characters)

    # If the final string ends with '.', replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final formatted string
    print(final_string)

# Call the function to execute
format_string()
