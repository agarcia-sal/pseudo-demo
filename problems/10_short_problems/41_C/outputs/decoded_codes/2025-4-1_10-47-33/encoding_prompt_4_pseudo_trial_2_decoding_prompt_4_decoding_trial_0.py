def transform_user_input():
    # Read input from the user
    user_input = input()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    user_input = user_input.replace('dot', '.').replace('at', '@')

    # If the first character is '.', prepend 'dot'
    if user_input.startswith('.'):
        user_input = 'dot' + user_input[1:]

    # Initialize count for '@' symbols and a list to hold characters
    at_count = 0
    character_list = []

    # If the first character is '@', prepend 'at'
    if user_input.startswith('@'):
        user_input = 'at' + user_input[1:]

    # Iterate over each character in the modified input
    for character in user_input:
        # Check if the character is '@'
        if character == '@':
            if at_count > 0:
                # Append 'at' if it's not the first '@'
                character_list.append('at')
            else:
                # Append first '@' as is
                character_list.append('@')
                at_count += 1
        else:
            # Append non '@' characters to the list
            character_list.append(character)

    # Join the character list into a single string
    final_output = ''.join(character_list)

    # If the last character is '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'

    # Output the final modified string
    print(final_output)

# Call the function to execute the transformation
transform_user_input()
