def convert_input_to_email_format():
    # Read a line of input and remove leading and trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # If the first character is a dot, prepend "dot" to the string
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]
    
    # Initialize counter and conversion list
    counter = 0
    conversion_list = []
    
    # If the first character is an at symbol, prepend "at" to the string
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]
    
    # Iterate through each character in the modified input_string
    for character in input_string:
        if character == '@':
            # Check if an '@' was already added
            if counter > 0:
                conversion_list.append("at")
                counter = 1  # Track that we've added an '@'
            else:
                conversion_list.append("@")
                counter = 1
        else:
            conversion_list.append(character)
    
    # Join the list into a single string
    converted_string = ''.join(conversion_list)
    
    # If the last character of the converted string is a dot, replace it with "dot"
    if converted_string.endswith('.'):
        converted_string = converted_string[:-1] + "dot"
    
    # Output the final converted string
    print(converted_string)

# Call the function
convert_input_to_email_format()
