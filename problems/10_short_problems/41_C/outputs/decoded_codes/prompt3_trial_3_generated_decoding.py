# Function to process the input string according to specific rules
def process_input():
    # Read input from the user
    input_string = input()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is '.', prepend 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize a counter and an empty list to store characters
    counter = 0
    character_list = []

    # If the first character is '@', prepend 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Process each character in the modified input_string
    for character in input_string:
        if character == '@':
            if counter > 0:
                character_list.append('at')
                counter = 1
            else:
                character_list.append('@')
                counter = 1
        else:
            character_list.append(character)

    # Join the characters in character_list into a single string
    final_output = ''.join(character_list)

    # If the last character of final_output is '.', replace it with 'dot'
    if final_output.endswith('.'):
        final_output = final_output[:-1] + 'dot'

    # Output the final processed string
    print(final_output)

# Calling the function to execute the process
process_input()
