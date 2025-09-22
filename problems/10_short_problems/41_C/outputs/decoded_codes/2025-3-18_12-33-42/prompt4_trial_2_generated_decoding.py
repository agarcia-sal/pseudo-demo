def process_input():
    # Read input from user
    input_line = input()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@' in the input
    input_line = input_line.replace('dot', '.')
    input_line = input_line.replace('at', '@')

    # If the first character is '.', prepend 'dot'
    if input_line.startswith('.'):
        input_line = 'dot' + input_line[1:]

    # Initialize counter and list for output characters
    counter = 0
    output_list = []

    # If the first character is '@', prepend 'at'
    if input_line.startswith('@'):
        input_line = 'at' + input_line[1:]

    # Process each character in the modified input
    for character in input_line:
        if character == '@':
            # If '@' has already been added, append 'at' to output list
            if counter > 0:
                output_list.append('at')
                counter = 1
            else:
                output_list.append('@')
                counter = 1
        else:
            # Add the character to the output list
            output_list.append(character)
            counter = 0  # Reset counter for other characters

    # Join the output list into a single string
    output_string = ''.join(output_list)

    # If the last character is '.', replace it with 'dot'
    if output_string.endswith('.'):
        output_string = output_string[:-1] + 'dot'

    # Print the final processed string
    print(output_string)

# Call the function to execute
process_input()
