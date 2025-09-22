def transform_input_string():
    # Read input from standard input
    input_string = input()

    # Clean up the input by replacing specific words with symbols
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # If the first character is a dot, prepend 'dot' to the string
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize counters and placeholder
    counter = 0
    modified_list = []
    
    # If the first character is '@', prepend 'at' to the string
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the modified input_string
    for character in input_string:
        if character == '@':
            # Check if '@' has been used before
            if counter > 0:
                modified_list.append('at')
                counter = 1
            else:
                modified_list.append('@')
                counter = 1
        else:
            modified_list.append(character)

    # Join the modified list into a single string
    output_string = ''.join(modified_list)

    # If the last character is a dot, replace it with 'dot'
    if output_string.endswith('.'):
        output_string = output_string[:-1] + 'dot'
    
    # Print the final transformed string
    print(output_string)

# Call the function to execute the transformation
transform_input_string()
