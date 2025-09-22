def process_input():
    # Read a line of input and remove leading/trailing spaces
    line_of_text = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    line_of_text = line_of_text.replace('dot', '.').replace('at', '@')

    # If the first character is a '.', prepend 'dot' to the string
    if line_of_text.startswith('.'):
        line_of_text = 'dot' + line_of_text[1:]

    # Initialize a counter and a list to hold the modified characters
    character_counter = 0
    modified_characters = []

    # If the first character is '@', prepend 'at' to the string
    if line_of_text.startswith('@'):
        line_of_text = 'at' + line_of_text[1:]

    # Iterate through each character in line_of_text
    for character in line_of_text:
        if character == '@':
            # Check how many '@' have been processed
            if character_counter > 0:
                modified_characters.append('at')
                character_counter = 1
            else:
                modified_characters.append('@')
                character_counter = 1
        else:
            # Add the current character to the list of modified characters
            modified_characters.append(character)

    # Join all characters in modified_characters to create a string
    final_output = ''.join(modified_characters)

    # If the last character is a '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'

    # Output the final modified string
    print(final_output)

# Uncomment the below line to call the function directly or use it in tests
# process_input()
