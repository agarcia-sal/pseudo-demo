def process_input():
    # Step 1: Read the input and remove surrounding whitespace
    user_input = input().strip()

    # Step 2: Replace occurrences of 'dot' with '.' and 'at' with '@'
    user_input = user_input.replace('dot', '.').replace('at', '@')

    # Step 3: If the string starts with a '.', prepend 'dot' to the string
    if user_input.startswith('.'):
        user_input = 'dot' + user_input[1:]

    # Step 4: Initialize variables to track symbols and processed characters
    symbol_counter = 0
    processed_characters = []
    
    # Step 5: If the string starts with '@', prepend 'at' to the string
    if user_input.startswith('@'):
        user_input = 'at' + user_input[1:]

    # Step 6: Process each character in the user_input string
    for character in user_input:
        # Check for the presence of the '@' character
        if character == '@':
            if symbol_counter > 0:
                # Previous '@' encountered, add 'at' to the list
                processed_characters.append('at')
            # Append '@'
            processed_characters.append('@')
            symbol_counter += 1
        else:
            # Append any other character to the processed characters
            processed_characters.append(character)

    # Step 7: Convert the processed characters list back into a string
    processed_string = ''.join(processed_characters)

    # Step 8: If the final string ends with '.', replace it with 'dot'
    if processed_string.endswith('.'):
        processed_string = processed_string[:-1] + 'dot'

    # Step 9: Output the final processed string
    print(processed_string)

# Call the function to execute
process_input()
