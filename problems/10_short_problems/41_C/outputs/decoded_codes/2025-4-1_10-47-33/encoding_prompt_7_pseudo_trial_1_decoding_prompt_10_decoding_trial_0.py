def convert_input_to_email_format():
    # Read a line of input and remove leading and trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # If the first character is a dot, prepend "dot"
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]
    
    # Initialize a counter and a list to build the converted string
    counter = 0
    conversion_list = []
    
    # If the first character is an '@', prepend "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Process each character in the input_string
    for character in input_string:
        if character == '@':
            # If an '@' was already added, use "at"
            if counter > 0:
                conversion_list.append("at")
            else:
                conversion_list.append("@")
            # Track that we've added an '@'
            counter += 1
        else:
            conversion_list.append(character)
    
    # Join the list into a single string
    converted_string = ''.join(conversion_list)
    
    # If the last character of the converted string is a dot, replace it with "dot"
    if converted_string.endswith('.'):
        converted_string = converted_string[:-1] + "dot"
    
    # Output the final converted string
    print(converted_string)

# Example invocation of the function (uncomment the next line to test)
# convert_input_to_email_format()
