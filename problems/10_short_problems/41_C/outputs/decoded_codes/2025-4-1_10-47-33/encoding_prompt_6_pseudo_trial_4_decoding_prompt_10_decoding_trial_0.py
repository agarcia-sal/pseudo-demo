def process_input_string():
    # Read input from the user
    input_string = input()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')
    
    # Check if the first character is a dot and update accordingly
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize counter for '@' occurrences and an empty list for characters
    occurrence_counter = 0
    character_list = []

    # Check if the first character is an '@' and update accordingly
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Loop through each character in the modified input string
    for character in input_string:
        if character == '@':
            if occurrence_counter > 0:
                character_list.append('at')
                occurrence_counter = 1  # Update counter
            else:
                character_list.append('@')
                occurrence_counter = 1  # Update counter
        else:
            character_list.append(character)

    # Join the list of characters into a single string
    result_string = ''.join(character_list)

    # Check if the last character is a dot and update accordingly
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'

    # Print the final modified string
    print(result_string)

# Run the function to process input
process_input_string()
