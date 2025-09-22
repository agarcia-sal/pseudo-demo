def convert_input_to_email_format():
    # Read a line of input and remove leading and trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Handle edge case for starting with '.'
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]
    
    counter = 0  # To track if we've added an '@'
    conversion_list = []  # To build the final output
    length = len(input_string)

    # Handle edge case for starting with '@'
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]
    
    # Iterate through each character in the modified input_string
    for character in input_string:
        if character == '@':
            if counter > 0:
                conversion_list.append("at")
                counter = 1  # Track that we've added an '@'
            else:
                conversion_list.append("@")
                counter = 1
        else:
            conversion_list.append(character)
    
    # Convert the list to a string
    converted_string = ''.join(conversion_list)

    # Handle edge case for ending with '.'
    if converted_string.endswith('.'):
        converted_string = converted_string[:-1] + "dot"
    
    # Output the final converted string
    print(converted_string)

# Call the function to execute
convert_input_to_email_format()
